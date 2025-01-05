const businessTypeSelect = document.getElementById('business_type');
const proprietorshipForm = document.getElementById('proprietorship_form');

// Event listener to display the form dynamically
businessTypeSelect.addEventListener('change', () => {
    if (businessTypeSelect.value === 'Proprietorship') {
        proprietorshipForm.classList.remove('hidden');
    } else {
        proprietorshipForm.classList.add('hidden');
    }
});