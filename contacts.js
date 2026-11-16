/**
 * =========================================================================
 * TOP CUTE GIRLS - DYNAMIC CONTACT NUMBER BINDING SYSTEM
 * =========================================================================
 * Fetches the master contact variable for this page and dynamically binds
 * it to all contact entries (headers, companion cards, footers, schema,
 * and fixed floating Call / WhatsApp action buttons).
 * Master variable value is defined & controlled by the Admin Panel.
 */

(function () {
  'use strict';

  function applyContactVariable() {
    if (!window.PAGE_CONTACT) {
      return;
    }

    // 1. Check if the Admin Panel defined an updated master value in localStorage
    try {
      const stored = localStorage.getItem('tcg_admin_contacts_v1');
      if (stored) {
        const allContacts = JSON.parse(stored);
        const pageId = window.PAGE_CONTACT.id || window.location.pathname.split('/').pop().replace('.html', '');
        if (allContacts && allContacts[pageId]) {
          const item = allContacts[pageId];
          if (item.phone) window.PAGE_CONTACT.phone = item.phone;
          if (item.whatsapp) window.PAGE_CONTACT.whatsapp = item.whatsapp;
          if (item.display_format) {
            window.PAGE_CONTACT.display = item.display_format;
          } else if (item.phone) {
            window.PAGE_CONTACT.display = '+91-' + item.phone;
          }
        }
      }
    } catch (e) {
      // Storage unavailable or cross-origin - fallback to inline master variable
    }

    const phone = window.PAGE_CONTACT.phone || '000000000';
    const whatsapp = window.PAGE_CONTACT.whatsapp || ('91' + phone);
    const display = window.PAGE_CONTACT.display || ('+91-' + phone);

    // 2. Bind to all telephone links on the page (Header, Mobile Menu, Cards, Footer)
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
      link.href = 'tel:' + phone;
      
      // Update any child text element displaying the phone number
      const span = link.querySelector('span');
      if (span) {
        const txt = span.textContent.trim();
        if (/Call \+91/i.test(txt)) {
          span.textContent = 'Call ' + display;
        } else if (/\+91/i.test(txt) || /[0-9]{10}/.test(txt)) {
          span.textContent = display;
        }
      }
    });

    // 3. Bind to all WhatsApp links on the page (preserving specific girl names in query params)
    document.querySelectorAll('a[href*="wa.me/"]').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const questionIndex = href.indexOf('?');
      const query = questionIndex !== -1 ? href.substring(questionIndex) : '';
      link.href = 'https://wa.me/' + whatsapp + query;
    });

    // 4. Bind specifically to floating action buttons
    const floatCall = document.getElementById('floating-call-btn');
    if (floatCall) {
      floatCall.href = 'tel:' + phone;
    }
    const floatWa = document.getElementById('floating-whatsapp-btn');
    if (floatWa) {
      floatWa.href = 'https://wa.me/' + whatsapp;
    }

    // 5. Bind to any explicit contact data elements
    document.querySelectorAll('[data-contact="phone"]').forEach(el => el.textContent = phone);
    document.querySelectorAll('[data-contact="whatsapp"]').forEach(el => el.textContent = '+' + whatsapp);
    document.querySelectorAll('[data-contact="display"]').forEach(el => el.textContent = display);

    // 6. Bind to JSON-LD SEO structured data schema
    document.querySelectorAll('script[type="application/ld+json"]').forEach(script => {
      try {
        const text = script.textContent;
        if (text.includes('"telephone"')) {
          script.textContent = text.replace(/"telephone":\s*"[^"]+"/g, `"telephone": "${display}"`);
        }
      } catch (e) {}
    });

    // 7. Ensure Lucide icons are rendered for dynamic elements
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  // Execute immediately if DOM is ready, or listen for DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyContactVariable);
  } else {
    applyContactVariable();
  }

  // Globally exposed updater function
  window.refreshContactNumbers = applyContactVariable;
})();
