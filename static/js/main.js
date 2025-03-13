// SGEIB - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Handle search form submission
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const searchInput = document.getElementById('searchInput');
            if (searchInput.value.trim() === '') {
                e.preventDefault();
                showAlert('Please enter a search term', 'warning');
            }
        });
    }

    // Handle query form submission
    const queryForm = document.getElementById('queryForm');
    if (queryForm) {
        queryForm.addEventListener('submit', function(e) {
            const queryInput = document.getElementById('query_text');
            if (queryInput.value.trim().length < 10) {
                e.preventDefault();
                showAlert('Your query should be at least 10 characters long', 'warning');
            }
        });
    }

    // Handle report form submission
    const reportForm = document.getElementById('reportForm');
    if (reportForm) {
        reportForm.addEventListener('submit', function(e) {
            const titleInput = document.getElementById('title');
            const descriptionInput = document.getElementById('description');
            
            if (titleInput.value.trim().length < 5) {
                e.preventDefault();
                showAlert('Report title should be at least 5 characters long', 'warning');
                return;
            }
            
            if (descriptionInput.value.trim().length < 20) {
                e.preventDefault();
                showAlert('Report description should be at least 20 characters long', 'warning');
                return;
            }
            
            // Show loading indicator
            showLoading('Generating your report. This may take a moment...');
        });
    }

    // Function to show alerts
    window.showAlert = function(message, type = 'info') {
        const alertPlaceholder = document.getElementById('alertPlaceholder');
        if (alertPlaceholder) {
            const wrapper = document.createElement('div');
            wrapper.innerHTML = `
                <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                    ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            `;
            alertPlaceholder.append(wrapper);
            
            // Auto-dismiss after 5 seconds
            setTimeout(() => {
                const alert = new bootstrap.Alert(wrapper.querySelector('.alert'));
                alert.close();
            }, 5000);
        }
    };

    // Function to show loading indicator
    window.showLoading = function(message = 'Loading...') {
        const loadingPlaceholder = document.getElementById('loadingPlaceholder');
        if (loadingPlaceholder) {
            loadingPlaceholder.innerHTML = `
                <div class="d-flex justify-content-center my-4">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <span class="ms-3">${message}</span>
                </div>
            `;
            loadingPlaceholder.style.display = 'block';
        }
    };

    // Function to hide loading indicator
    window.hideLoading = function() {
        const loadingPlaceholder = document.getElementById('loadingPlaceholder');
        if (loadingPlaceholder) {
            loadingPlaceholder.style.display = 'none';
            loadingPlaceholder.innerHTML = '';
        }
    };

    // Handle knowledge base category selection
    const categorySelect = document.getElementById('categorySelect');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            window.location.href = `/knowledge-base?category=${this.value}`;
        });
    }

    // Handle trend forecaster category selection
    const trendCategorySelect = document.getElementById('trendCategorySelect');
    if (trendCategorySelect) {
        trendCategorySelect.addEventListener('change', function() {
            window.location.href = `/trend-forecaster?category=${this.value}`;
        });
    }

    // Toggle password visibility
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function() {
            const passwordField = document.getElementById(this.dataset.target);
            const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordField.setAttribute('type', type);
            
            // Toggle the icon
            this.querySelector('i').classList.toggle('bi-eye');
            this.querySelector('i').classList.toggle('bi-eye-slash');
        });
    });

    // Handle response copy to clipboard
    const copyButtons = document.querySelectorAll('.copy-response');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const responseText = document.getElementById(this.dataset.target).innerText;
            navigator.clipboard.writeText(responseText).then(() => {
                showAlert('Response copied to clipboard!', 'success');
            }).catch(err => {
                console.error('Could not copy text: ', err);
                showAlert('Failed to copy response', 'danger');
            });
        });
    });
});
