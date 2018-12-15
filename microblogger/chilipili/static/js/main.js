

$('#like-button').on('click', function (event) {
    event.preventDefault()
    const csrfToken = $(event.target).find('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        method: 'POST',
        url: event.target.action,
        data: {
            'csrfmiddlewaretoken': csrfToken
        },
        sucess: function (results) {
            if (results.like) {
                var likes = likes + 1
            }
        }

    })


})

// $('.toggle-favorite-form').on('submit', function (event) {
//     event.preventDefault()
//     const csrfToken = $(event.target).find('[name=csrfmiddlewaretoken]').val()
//     $.ajax({
//         method: 'POST',
//         url: event.target.action,
//         data: {
//             'csrfmiddlewaretoken': csrfToken
//         },
//         success: function (results) {
//             let starToUse
//             if (results.favorite) {
//                 starToUse = FILLED_IN_STAR
//             } else {
//                 starToUse = EMPTY_STAR
//             }
//             $(event.target).find('button[type=submit]').html(starToUse)

//             $(`#book-${results.book_id}`).find('.book-num-favorites').text(
//                 `Favorited ${pluralize(results.num_of_favorites, 'time')}`
//             )
//         }
//     })
// })