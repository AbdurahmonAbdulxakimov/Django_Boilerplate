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
    })
}

$(document).ready(function () {
    // Regular expressions to match element IDs
    const content_item_regex = /^id_items-(\d+)-content_item_type$/;
    const video_type_regex = /^id_items-(\d+)-video_type$/;

    // Check for changes in the select elements every 100 milliseconds
    setInterval(function () {
        let selects = Array.from(document.querySelectorAll("select"));
        selects.forEach(select => {
            let match1 = select.id.match(content_item_regex);
            let match2 = select.id.match(video_type_regex);
            if (match1) {
                let order = match1[1];
                switch (select.value) {
                    case "photo":
                        change_elements_visibility(order, ["photo", "photo_author", "photo_size"], ["video_type", "video_link", "video_file", "text_uz", "text_ru", "text_en", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo", "news_content"]);
                        break;
                    case "text":
                        change_elements_visibility(order, ["text_uz", "text_ru", "text_en"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo", "news_content"]);
                        break;
                    case "quote":
                        change_elements_visibility(order, ["quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "text_en", "news_content"]);
                        break;
                    case "news":
                        change_elements_visibility(order, ["news_content"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "text_en", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo"]);
                        break;
                    default:
                        change_elements_visibility(order, [], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "text_en", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo", "news_content"]);
                        break;
                }
            } else if (match2) {
                let order = match2[1];
                let content_item_type_value = document.querySelector(`select#id_items-${order}-content_item_type`).value;
                if (content_item_type_value === "video") {
                    switch (select.value) {
                        case "upload":
                            change_elements_visibility(order, ["video_file"], ["video_link"]);
                            break;
                        case "link":
                            change_elements_visibility(order, ["video_link"], ["video_file"]);
                            break;
                    }
                }
            }
        })
    }, 100);

    // Event listener for the 'change' event on select elements
    $(document).on('change', 'select', function () {
        let match1 = this.id.match(content_item_regex);
        let match2 = this.id.match(video_type_regex);

        if (match1) {
            let order = match1[1];
            switch (this.value) {
                case "photo":
                    change_elements_visibility(order, ["photo", "photo_author", "photo_size"], ["video_type", "video_link", "video_file", "text_uz", "text_ru", "text_en", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo", "news_content"]);
                    break;
                case "text":
                    change_elements_visibility(order, ["text_uz", "text_ru", "text_en"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo", "news_content"]);
                    break;
                case "quote":
                    change_elements_visibility(order, ["quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "text_en", "news_content"]);
                    break;
                case "news":
                    change_elements_visibility(order, ["news_content"], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "text_en", "quote_uz", "quote_ru", "quote_en", "quote_author", "quote_photo"]);
                    break;
                default:
                    change_elements_visibility(order, [], ["video_type", "video_link", "video_file", "photo", "photo_author", "photo_size", "text_uz", "text_ru", "quote_uz", "quote_ru", "quote_author", "quote_photo", "news_content"]);
                    break;
            }
        } else if (match2) {
            let order = match2[1];
            switch (this.value) {
                case "upload":
                    change_elements_visibility(order, ["video_file"], ["video_link"]);
                    break;
                case "link":
                    change_elements_visibility(order, ["video_link"], ["video_file"]);
            }
        }
    });
});
