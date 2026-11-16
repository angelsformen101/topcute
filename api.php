<?php
/**
 * TOP CUTE GIRLS - ROOT API FORWARDER
 * Forwards any direct /api.php requests to /admin/api.php
 */
if (file_exists(__DIR__ . '/admin/api.php')) {
    require_once __DIR__ . '/admin/api.php';
} else {
    http_response_code(404);
    header('Content-Type: application/json');
    echo json_encode(['status' => 'error', 'message' => 'API endpoint not found.']);
}
