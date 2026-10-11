/**
 * NCERC College Chatbot Administration Dashboard - Core Interactive Scripts
 * Phase 1: Navigation, Instant Filtering, Mobile Drawer & Staged Action Handling
 */

document.addEventListener('DOMContentLoaded', function () {
  initNavigation();
  initMobileDrawer();
  initTableSearch();
  initActionAlerts();
});

// View Navigation Map
const viewTitles = {
  'overview': 'Executive Administration Overview',
  'knowledge': 'Knowledge Base Management',
  'add': 'Create Knowledge Record',
  'import': 'Dataset Bulk Ingestion',
  'notices': 'Institutional Notice Management',
  'ai-drafts': 'Gemini AI Draft Review Workspace'
};

function initNavigation() {
  const navButtons = document.querySelectorAll('.nav-item-btn');
  const panes = document.querySelectorAll('.tab-pane');
  const titleElem = document.getElementById('currentViewTitle');
  const breadcrumbElem = document.getElementById('viewBreadcrumb');

  function switchTab(targetView) {
    if (!targetView) return;

    // Update nav buttons
    navButtons.forEach(btn => {
      if (btn.getAttribute('data-view') === targetView) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Update content panes
    panes.forEach(pane => {
      if (pane.id === `view-${targetView}`) {
        pane.classList.add('active');
      } else {
        pane.classList.remove('active');
      }
    });

    // Update Header Title & Breadcrumb
    if (titleElem && viewTitles[targetView]) {
      titleElem.textContent = viewTitles[targetView];
    }
    if (breadcrumbElem) {
      breadcrumbElem.textContent = `Admin Console / ${viewTitles[targetView] || targetView}`;
    }

    // Close mobile drawer if open
    closeMobileDrawer();

    // Scroll to top of content
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  navButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const targetView = this.getAttribute('data-view');
      switchTab(targetView);
    });
  });

  // Shortcut action buttons in overview
  const shortcutButtons = document.querySelectorAll('[data-shortcut-target]');
  shortcutButtons.forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const targetView = this.getAttribute('data-shortcut-target');
      switchTab(targetView);
    });
  });
}

function initMobileDrawer() {
  const toggleBtn = document.getElementById('sidebarToggle');
  const sidebar = document.getElementById('adminSidebar');
  const backdrop = document.getElementById('sidebarBackdrop');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      if (backdrop) backdrop.classList.toggle('active');
    });
  }

  if (backdrop && sidebar) {
    backdrop.addEventListener('click', closeMobileDrawer);
  }
}

function closeMobileDrawer() {
  const sidebar = document.getElementById('adminSidebar');
  const backdrop = document.getElementById('sidebarBackdrop');
  if (sidebar) sidebar.classList.remove('open');
  if (backdrop) backdrop.classList.remove('active');
}

function initTableSearch() {
  const searchInput = document.getElementById('tableSearch');
  const categorySelect = document.getElementById('categoryFilter');
  const tableRows = document.querySelectorAll('#knowledgeTableBody tr');
  const visibleCountElem = document.getElementById('visibleCount');
  const noResultsState = document.getElementById('noResultsState');

  if (!tableRows.length) return;

  function filterRows() {
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const selectedCategory = (categorySelect ? categorySelect.value : 'all').toLowerCase();

    let visibleCount = 0;

    tableRows.forEach(row => {
      const category = (row.getAttribute('data-category') || '').toLowerCase();
      const textContent = row.textContent.toLowerCase();

      const matchesCategory = (selectedCategory === 'all' || category === selectedCategory);
      const matchesQuery = (!query || textContent.includes(query));

      if (matchesCategory && matchesQuery) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    if (visibleCountElem) {
      visibleCountElem.textContent = visibleCount;
    }

    if (noResultsState) {
      noResultsState.style.display = (visibleCount === 0) ? 'block' : 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterRows);
  }
  if (categorySelect) {
    categorySelect.addEventListener('change', filterRows);
  }
}

function initActionAlerts() {
  // Staged feature notifications for buttons in Phase 1
  const stagedButtons = document.querySelectorAll('.staged-action-btn');
  stagedButtons.forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const featureName = this.getAttribute('data-feature') || 'This action';
      alert(`${featureName} is staged for Phase 2. Database records and configuration remain protected.`);
    });
  });
}
