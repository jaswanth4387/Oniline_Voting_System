document.addEventListener("DOMContentLoaded", () => {

    animateVoteCards();

});


/* ================================
   VOTE CARD ANIMATION
================================ */

function animateVoteCards() {

    const cards = document.querySelectorAll('.candidate-card');

    cards.forEach(card => {

        card.addEventListener('mouseenter', () => {

            card.style.transform = 'scale(1.02)';

        });

        card.addEventListener('mouseleave', () => {

            card.style.transform = 'scale(1)';

        });

    });

}