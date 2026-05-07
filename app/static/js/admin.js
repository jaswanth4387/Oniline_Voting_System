document.addEventListener("DOMContentLoaded", () => {

    initDeleteConfirm();

});


/* ================================
   DELETE CONFIRMATION
================================ */

function initDeleteConfirm() {

    const deleteButtons =
        document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {

        button.addEventListener('click', (e) => {

            const confirmDelete = confirm(
                'Are you sure you want to delete this candidate?'
            );

            if (!confirmDelete) {

                e.preventDefault();

            }

        });

    });

}