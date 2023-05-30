// solucion en js


let arraynumeros=[];

let cantidad=parseInt(prompt("ingresa la cantidad de numeros"));

for (i=cantidad;i>0; i--){
    let numeros=parseInt(prompt("ingresa un numero"))
    
    arraynumeros.push(numeros)
}



alert(`el numero mayor es ${Math.max(...arraynumeros)}`)
console.log(arraynumeros);