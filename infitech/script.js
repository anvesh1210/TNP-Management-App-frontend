function setupNavigationButton(buttonId, targetUrl) {
    const button = document.getElementById(buttonId);
    if (!button) {
        console.error(`Button with ID "${buttonId}" not found.`);
        return;
    }

    button.addEventListener('click', function () {
        window.location.href = targetUrl;
    });
}

// When the DOM is fully loaded, then call the setup function
document.addEventListener("DOMContentLoaded", function () {
    setupNavigationButton('topicsButton', 'topics.html');
});