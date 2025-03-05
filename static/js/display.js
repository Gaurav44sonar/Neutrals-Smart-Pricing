
function redirectToProduct(button) {
    let card = button.closest(".card"); // Find the closest card container

    let productName = card.querySelector(".product-name").innerText;
    let productWeight = card.querySelector(".product-weight").innerText;
    let productPrice = card.querySelector(".price").innerText;
    let productImage = card.querySelector("img").src;

    // Encode data as URL parameters
    let url = `product.html?name=${encodeURIComponent(productName)}&weight=${encodeURIComponent(productWeight)}&price=${encodeURIComponent(productPrice)}&image=${encodeURIComponent(productImage)}`;

    window.location.href = url; // Redirect to product.html with data
}
