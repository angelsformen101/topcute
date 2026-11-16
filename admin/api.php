<?php
/**
 * =========================================================================
 * TOP CUTE GIRLS - ADMIN API CONTROLLER
 * =========================================================================
 * Handles saving contact numbers, authentication, session tokens,
 * and synchronizing master variables into contacts-config.js, contacts.json,
 * and config.json.
 */
header('Content-Type: application/json');

define('ROOT_DIR', dirname(__DIR__));
define('DATA_DIR', __DIR__ . DIRECTORY_SEPARATOR . 'data');
define('CONTACTS_FILE', DATA_DIR . DIRECTORY_SEPARATOR . 'contacts.json');
define('CONFIG_FILE', DATA_DIR . DIRECTORY_SEPARATOR . 'config.json');
define('CONFIG_JS_FILE', ROOT_DIR . DIRECTORY_SEPARATOR . 'contacts-config.js');

// 15 Protected pages that MUST NOT be touched
define('UNTOUCHED_PAGES', [
    'rudrapur.html',
    'ramnagar.html',
    'himachal.html',
    'manali.html',
    'rishikesh.html',
    'mussoorie.html',
    'index.html',
    'gurgaon.html',
    'indore.html',
    'ghaziabad.html',
    'chandigarh.html',
    'bangalore.html',
    'mumbai.html',
    'delhi.html',
    'dehradun.html'
]);

// Ensure data directory exists
if (!is_dir(DATA_DIR)) {
    @mkdir(DATA_DIR, 0755, true);
}

function get_config() {
    $default = [
        'admin_username' => 'admin',
        'admin_password_hash' => '$2y$10$V9pI6kRNdCkEo7GLITUsueCpcjNRA1Cc3GmWKz/8HJb9H4niHlxoW',
        'pass_sha256' => 'dd16d17cdef7b1a9ab0f2e0885019af639e9657c2a2a5a6e294f86aa4e69d5da',
        'site_title' => 'Top Cute Girls - Admin Control Panel',
        'last_updated' => date('Y-m-d H:i:s')
    ];
    if (file_exists(CONFIG_FILE)) {
        $data = json_decode(@file_get_contents(CONFIG_FILE), true);
        if (is_array($data)) {
            return array_merge($default, $data);
        }
    }
    return $default;
}

function save_config($cfg) {
    return @file_put_contents(CONFIG_FILE, json_encode($cfg, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX) !== false;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $raw = file_get_contents('php://input');
    $payload = json_decode($raw, true);

    if ($payload && isset($payload['action'])) {
        $action = $payload['action'];

        // 1. Action: Change Password
        if ($action === 'change_password') {
            $current_pass = $payload['current_password'] ?? '';
            $new_pass = $payload['new_password'] ?? '';
            $new_sha256 = $payload['pass_sha256'] ?? '';

            $cfg = get_config();
            $hash = $cfg['admin_password_hash'] ?? '';
            $pass_sha = $cfg['pass_sha256'] ?? '';

            // Verify current password
            $current_sha = hash('sha256', $current_pass . '_tcg_salt_2026');
            $is_valid = password_verify($current_pass, $hash) || ($current_sha === $pass_sha) || ($current_pass === 'admin123' && empty($pass_sha));

            if (!$is_valid) {
                http_response_code(400);
                echo json_encode(['status' => 'error', 'message' => 'Current password is incorrect.']);
                exit;
            }

            if (strlen($new_pass) < 6) {
                http_response_code(400);
                echo json_encode(['status' => 'error', 'message' => 'New password must be at least 6 characters.']);
                exit;
            }

            $cfg['admin_password_hash'] = password_hash($new_pass, PASSWORD_BCRYPT);
            $cfg['pass_sha256'] = $new_sha256 ?: hash('sha256', $new_pass . '_tcg_salt_2026');
            $cfg['last_updated'] = date('Y-m-d H:i:s');
            save_config($cfg);

            echo json_encode(['status' => 'success', 'message' => 'Admin password updated successfully across all devices.', 'pass_sha256' => $cfg['pass_sha256']]);
            exit;
        }

        // 2. Action: Login & Issue Session ID
        if ($action === 'login') {
            $user = trim($payload['username'] ?? '');
            $pass = trim($payload['password'] ?? '');

            $cfg = get_config();
            $valid_user = ($user === ($cfg['admin_username'] ?? 'admin'));
            $pass_sha = $cfg['pass_sha256'] ?? '';
            $hash = $cfg['admin_password_hash'] ?? '';
            $input_sha = hash('sha256', $pass . '_tcg_salt_2026');

            $valid_pass = password_verify($pass, $hash) || ($input_sha === $pass_sha);

            if ($valid_user && $valid_pass) {
                $session_id = 'tcg_sess_' . bin2hex(random_bytes(16));
                $expires_in = 900; // 15 minutes of inactivity

                echo json_encode([
                    'status' => 'success',
                    'message' => 'Login successful.',
                    'session_id' => $session_id,
                    'expires_in' => $expires_in,
                    'user' => $user
                ]);
                exit;
            } else {
                http_response_code(401);
                echo json_encode(['status' => 'error', 'message' => 'Invalid username or password.']);
                exit;
            }
        }
        
        // 3. Action: Sync All Contacts
        if ($action === 'sync_all' && !empty($payload['data'])) {
            $data = $payload['data'];
            
            // Save to contacts.json
            @file_put_contents(CONTACTS_FILE, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);

            // Save to contacts-config.js
            $config_export = [];
            foreach ($data as $id => $p) {
                $config_export[$id] = [
                    'phone' => $p['phone'] ?? '000000000',
                    'whatsapp' => $p['whatsapp'] ?? '91000000000',
                    'display' => $p['display_format'] ?? ('+91-' . ($p['phone'] ?? '000000000'))
                ];
            }
            $js_content = "/**\n * TOP CUTE GIRLS - MASTER CONTACT CONFIGURATION REGISTRY\n * Generated by Admin Panel\n */\nwindow.SITE_CONTACTS = " . json_encode($config_export, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . ";\n";
            @file_put_contents(CONFIG_JS_FILE, $js_content, LOCK_EX);

            // Update master variable in allowed HTML files
            foreach ($data as $id => $p) {
                $filename = ($p['filename'] ?? ($id . '.html'));
                
                // STRICT CHECK: Skip untouched pages
                if (in_array(strtolower($filename), array_map('strtolower', UNTOUCHED_PAGES))) {
                    continue;
                }

                $file_path = ROOT_DIR . DIRECTORY_SEPARATOR . $filename;
                if (file_exists($file_path)) {
                    $html = file_get_contents($file_path);
                    if ($html !== false && strpos($html, 'window.PAGE_CONTACT') !== false) {
                        $pattern = '/window\.PAGE_CONTACT\s*=\s*\{.*?\};/s';
                        $replacement = "window.PAGE_CONTACT = " . json_encode([
                            'id' => $id,
                            'phone' => $p['phone'] ?? '000000000',
                            'whatsapp' => $p['whatsapp'] ?? '91000000000',
                            'display' => $p['display_format'] ?? ('+91-' . ($p['phone'] ?? '000000000'))
                        ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . ";";

                        $new_html = preg_replace($pattern, $replacement, $html);
                        if ($new_html && $new_html !== $html) {
                            file_put_contents($file_path, $new_html, LOCK_EX);
                        }
                    }
                }
            }

            echo json_encode(['status' => 'success', 'message' => 'Master variables synchronized successfully.']);
            exit;
        }
    }
}

// GET Requests
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $q = $_GET['action'] ?? '';
    if ($q === 'config') {
        $cfg = get_config();
        echo json_encode([
            'username' => $cfg['admin_username'] ?? 'admin',
            'pass_sha256' => $cfg['pass_sha256'] ?? 'dd16d17cdef7b1a9ab0f2e0885019af639e9657c2a2a5a6e294f86aa4e69d5da',
            'last_updated' => $cfg['last_updated'] ?? ''
        ]);
        exit;
    }

    if (file_exists(CONTACTS_FILE)) {
        echo file_get_contents(CONTACTS_FILE);
    } else {
        echo json_encode([]);
    }
    exit;
}

echo json_encode(['status' => 'error', 'message' => 'Invalid request.']);
