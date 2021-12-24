
class CardItem extends HTMLElement{
    connectedCallback(){
        this.src = this.getAttribute("src") || null;
        this.name = this.getAttribute("name") || null;
        this.position = this.getAttribute("position") || null;
        this.text = this.getAttribute("text") || null;

        this.innerHTML=`
            <div class="card" data-tilt>
                <div class="card-img-wrapper">
                <img src="${this.src}" alt="">
                </div>
                <div class="card-info">
                <h2>${this.name}</h2>
                <h3>${this.position}</h3>
                <p>
                    "${this.text}"
                </p>
                <button>Read More</button>
                </div>
            </div>
            `;
    }
}

customElements.define("card-item", CardItem);