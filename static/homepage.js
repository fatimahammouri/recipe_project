// Homepage Java Script
// making the Cuisines List interactive


let listCuisineItems = document.querySelectorAll(".list_cuisine_item");
listCuisineItems.forEach((item, index)=>{
    item.addEventListener('click', (event)=>{
        let selectedCuisine = event.currentTarget.innerHTML;
        console.log(selectedCuisine)
        $.post('/results/'+ selectedCuisine ,(response)=>{
            $('#recipe_cards').html(response)
        }); 
    });
});