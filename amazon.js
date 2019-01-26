var product_info;
function get_product_info(){
    var upc;
    var model_number;
    var manufacturer;
    var title;
    var asin;
    var seller_id;
    if (document.URL.indexOf("/dp/") != -1){
        asin = document.URL.split("/dp/")[1].split("/")[0].split("?")[0]
    }else if (document.URL.indexOf("/gp/product/") != -1){
        asin = document.URL.split("/gp/product/")[1].split("/")[0].split("?")[0]
    }

    var sections = document.body.textContent.split("Item model number")
    if (sections.length > 1) {
        var t = sections[1]
        t = t.substr(0, 1000)
        t = t.replace("\n", " ").replace(":", "")
        var lines = t.split(/\s{2,}/).filter(Boolean);
        model_number = lines[0].trim()
    }
    var sections = document.body.textContent.split("ISBN-10")
    if (sections.length > 1) {
        var t = sections[1]
        t = t.substr(0, 1000)
        t = t.replace("\n", " ").replace(":", "")
        var lines = t.split(/\s+/).filter(Boolean);
        model_number = lines[0].trim()
    }
    var sections = document.body.textContent.split("UPC")
    if (sections.length > 1) {
        var t = sections[1]
        t = t.substr(0, 1000)
        t = t.replace("\n", " ").replace(":", "")
        var lines = t.split(/\s+/).filter(Boolean);
        upc = lines[0].trim()
    }

    var elem = document.getElementById('productTitle');    
    if (elem){
        title = elem.textContent.trim()
        var elem = document.getElementById('productDetails_detailBullets_sections1')
        if (elem){
            var aTags = elem.getElementsByTagName("th");
            for (var i = 0; i < aTags.length; i++){
                if (aTags[i].textContent.trim() == "Item model number"){
                    model_number = aTags[i].parentNode.getElementsByTagName("td")[0].textContent.trim()
                }
                if (aTags[i].textContent.trim() == "Manufacturer"){
                    manufacturer = aTags[i].parentNode.getElementsByTagName("td")[0].textContent.trim()
                }
            }
        }
    }

    if (!model_number){
        var elem = document.getElementById('detail-bullets')
        if (elem){
            var aTags = elem.getElementsByTagName("b");
            for (var i = 0; i < aTags.length; i++){
                if (aTags[i].textContent.trim() == "Item model number:"){
                    model_number = aTags[i].parentNode.textContent.replace("Item model number:", "").trim()
                }
                if (aTags[i].textContent.trim() == "Manufacturer:"){
                    manufacturer = aTags[i].parentNode.textContent.replace("Manufacturer:", "").trim()                
                }
            }
        }
    }

    if (model_number){
        var temp = model_number.split(" ")
        var longest = 0
        for (var i = 0; i < temp.length; i++){
            if (temp[i].length > longest){
                model_number = temp[i]
                longest = temp[i].length
            }
        }
    }

    var search = "";
    if (document.URL.indexOf("&field-keywords=") != -1){
        search = document.URL.split("&field-keywords=")[1].split("&")[0]    
    }else if (document.URL.indexOf("&keywords=") != -1){
        search = document.URL.split("&keywords=")[1].split("&")[0]    
    }

    search = search.replace(/\+/g, ' ');
    search = decodeURIComponent(search)

    var price;
    var price_elem = document.getElementById('priceblock_ourprice')
    if (!price_elem)
        price_elem = document.getElementById('priceblock_dealprice')
    if (price_elem)
        price = parseFloat(price_elem.textContent.replace(",", "").replace("$", ''))

    var seller_elem = document.getElementById('merchantID')
    if (seller_elem){
        seller_id = seller_elem.value
    }
    product_info = {
        "asin": asin,
        "upc": upc,
        "model_number": model_number,
        "manufacturer": manufacturer,
        "title": title,
        "full_title": title,
        "search": search,
        "url": document.URL,
        "doc_title": document.title,
        "price": price,
        "site": "amazon",
        "seller_id": seller_id
    }
    return product_info;
}