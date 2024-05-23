/**
 * Changes the visibility of elements based on the provided order number and lists of elements to show and hide.
 * @param {number} orderNumber - The order number of the elements.
 * @param {string[]} elementsToShow - An array of element classes to show.
 * @param {string[]} elementsToHide - An array of element classes to hide.
 */
function change_elements_visibility(orderNumber, elementsToShow, elementsToHide) {
    elementsToShow.forEach(item => {
        document.querySelector(`div#items-${orderNumber} div.field-${item}`).style.display = "block";
    });
    elementsToHide.forEach(item => {
        document.querySelector(`div#items-${orderNumber} div.field-${item}`).style.display = "none";
    });
}

$(document).ready(function () {
    // Regular expressions to match element IDs
    const contact_item_regex = /^id_items-(\d+)-type$/;

    // Check for changes in the select elements every 100 milliseconds
    setInterval(function () {
        let selects = Array.from(document.querySelectorAll("select"));
        selects.forEach(select => {
            let match = select.id.match(contact_item_regex);

            if (match) {
                let order = match[1];
                switch (select.value) {
                    case "phone":
                        change_elements_visibility(order, ["phone_number"], ["email", "link", "telegram_link"]);
                        break;
                    case "email":
                        change_elements_visibility(order, ["email"], ["phone_number", "link", "telegram_link"]);
                        break;
                    case "link":
                        change_elements_visibility(order, ["link"], ["phone_number", "email", "telegram_link"]);
                        break;
                    case "telegram":
                        change_elements_visibility(order, ["telegram_link"], ["phone_number", "email", "link"]);
                        break;
                    default:
                        change_elements_visibility(order, [], ["phone_number", "email", "link", "telegram_link"]);
                        break;
                }
            }

        })
    }, 100);

    // Event listener for the 'change' event on select elements
    $(document).on('change', 'select', function () {
        let match = this.id.match(contact_item_regex);

        if (match) {
            let order = match[1];
            switch (this.value) {
                case "phone":
                    change_elements_visibility(order, ["phone_number"], ["email", "link", "telegram_link"]);
                    break;
                case "email":
                    change_elements_visibility(order, ["email"], ["phone_number", "link", "telegram_link"]);
                    break;
                case "link":
                    change_elements_visibility(order, ["link"], ["phone_number", "email", "telegram_link"]);
                    break;
                case "telegram":
                    change_elements_visibility(order, ["telegram_link"], ["phone_number", "email", "link"]);
                    break;
                default:
                    change_elements_visibility(order, [], ["phone_number", "email", "link", "telegram_link"]);
                    break;
            }
        }
    });
});
