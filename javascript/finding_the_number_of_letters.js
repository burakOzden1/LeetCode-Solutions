let text = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veniam iusto cupiditate quas maxime beatae officiis aspernatur error ex porro modi."

let letter = prompt("please enter a letter : ");
let sonuc = bul(letter);

alert("Harf Sayısı : " + sonuc);

function bul(letter){
    let toplam = 0;
    for(let i=0; i<text.length; i++){
        if(text.charAt(i).toLowerCase()===letter.toLowerCase()){
            toplam += 1;
        }
    }
    return toplam
}