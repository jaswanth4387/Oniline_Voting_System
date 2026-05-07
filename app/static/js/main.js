document.addEventListener("DOMContentLoaded", () => {

    initVoteSystem();

    initAlerts();

});


/* ================================
   ALERTS
================================ */

function initAlerts() {

    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(alert => {

        setTimeout(() => {

            alert.style.display = 'none';

        }, 3000);

    });

}


/* ================================
   VOTING SYSTEM
================================ */

function initVoteSystem() {

    const cards = document.querySelectorAll('.candidate-card');

    let selectedId = null;


    // SELECT CANDIDATE

    cards.forEach(card => {

        card.addEventListener('click', () => {

            cards.forEach(c => {
                c.classList.remove('selected');
            });

            card.classList.add('selected');

            selectedId = card.dataset.id;

        });

    });


    // SUBMIT VOTE

    const submitBtn = document.querySelector('.submit-btn');

    if (submitBtn) {

        submitBtn.addEventListener('click', async (e) => {

            e.preventDefault();

            if (!selectedId) {

                alert('Please select a candidate');

                return;
            }

            try {

                const response = await fetch('/cast-vote', {

                    method: 'POST',

                    headers: {
                        'Content-Type': 'application/json'
                    },

                    body: JSON.stringify({
                        candidate_id: selectedId
                    })

                });

                const data = await response.json();

                if (response.ok) {

                    window.location.href = "/confirmation";

                } else {

                    alert(data.error);

                }

            } catch (error) {

                console.log(error);

                alert('Server error');

            }

        });

    }

}