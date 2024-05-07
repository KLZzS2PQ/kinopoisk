const btnSendreview = document.querySelector('.btn-send-review');
const btnsSendLike = document.querySelectorAll('.movie_review_card_form > button');
btnSendreview.addEventListener('click', (e) => {
    e.preventDefault();
    sendreview();
});


for (let i = 0; i < btnsSendLike.length; i++) {
    btnsSendLike[i].addEventListener('click', (e) => {
        e.preventDefault();
        sendLike(i);
    });
}


const movieIdInput = document.querySelector('input[name="movie_id"]');
const reviewInput = document.querySelector('textarea[name="review"]');
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]')


async function sendreview() {
    const result = await sendPost('/review/', {
        review: reviewInput.value,
        movie_id: movieIdInput.value,
        csrfmiddlewaretoken: csrfToken.value
    });
    // Отобразить элемент комментария.
}




async function sendLike(btnreviewLikeIndex) {
    const result = await sendPost('/add_review_like/', {
        review_id: btnsSendLike[btnreviewLikeIndex].parentNode.querySelector('input').value,
        csrfmiddlewaretoken: csrfToken.value
    });
    if (result['success'] === true) {
        const reviewLikeCountEl = btnsSendLike[btnreviewLikeIndex].parentNode.parentNode.querySelector('#review-likes-count')
        if (result['vote'] === true) {
            const imgLike = btnsSendLike[btnreviewLikeIndex].querySelector('img')
            imgLike.style.filter = 'none'
            reviewLikeCountEl.innerHTML = parseInt(reviewLikeCountEl.innerHTML) + 1
        }else {
            imgLike.style.filter = 'grayscale(1)'
            reviewLikeCountEl.innerHTML = parseInt(reviewLikeCountEl.innerHTML) - 1
        }
    }
}


const mcf = document.querySelector('.movie_review_card_form')
