

$('.like-button').on('click', function (event) {
    let parent_div = $(event.target).parents("div")[0];
    const csrfToken = $(parent_div).find('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        method: 'POST',
        url: parent_div.dataset["url"],
        data: {
            'csrfmiddlewaretoken': csrfToken
        }
    }).done(function (results) {
        if (results.likes) {
            $(parent_div).find('.like-count').text(results.likes);
        }
    });


})

$('.follow-button').on('click', function (event) {
    console.log(event)
    let parent_div = $(event.target).parents("div")[0];
    console.log(parent_div)
    const csrfToken = $(parent_div).find('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        method: 'POST',
        url: parent_div.dataset["url"],
        data: {
            'csrfmiddlewaretoken': csrfToken
        }
    }).done(function (results) {
        if (results.follows) {
            $(parent_div).find('.follow-count').text(results.follows);
        }
    });
})
