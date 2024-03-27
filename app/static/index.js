let predictButton = document.getElementById('predict')
let resultEl = document.getElementById('result')

const slider = document.getElementById('score')
const value =document.querySelector('.value')

value.textContent = slider.value
slider.oninput = function(){
    value.textContent = this.value
}

predictButton.addEventListener('click', (event) => {
    event.preventDefault()

    let formData = new FormData(document.getElementById('loan_form'))

    axios.post('/predict', formData)
        .then(response => {
            resultEl.innerHTML = response.data === '1' ? 'Yes' : 'No'
            resultEl.style.color = response.data === '1' ? "rgba(201, 0, 0)" : "rgba(11, 178, 14, 0.689)"
        })
})


