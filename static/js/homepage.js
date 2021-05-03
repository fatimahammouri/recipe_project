// Homepage Java Script
// making the Cuisines List interactive


let listCuisineItems = document.querySelectorAll(".list_cuisine_item");

listCuisineItems.forEach((item, index)=>{

    item.addEventListener("click", (event)=>{
        let selectedCuisine = event.currentTarget.innerHTML;
        console.log(selectedCuisine)
    
        const recipeCards = document.querySelector("#recipe_cards")
        $.post("/results/"+ selectedCuisine ,(response)=>{
            recipeCards.innerHTML = response;   
        }); 
    });
});