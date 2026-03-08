// Access the main app window
const main_window = window.parent.document.defaultView

main_window.addEventListener('beforeunload', function (event) {
    // Custom message (most browsers ignore it and show a default)   
    const message = ':( Are you sure you want to leave?';
    event.preventDefault();
    return message;
});