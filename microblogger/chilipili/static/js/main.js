function chilipiliHtml(chilipili) {
    return `
     <div class="chilipili-deets">
     <h4 class="username">${ chilipili.author_user}</h4>
     <p class="text">${ chilipili.text}</p> 

    <div class="chilipili-div" data-url="{% url 'like_chilipili' chilipili.pk %}">
        {% csrf_token %}
        <button class="btn like-button" ><i class="glyphicon glyphicon-thumbs-up"></i></button>
        <p>Likes: <span class="like-count">{{ chilipili.likes.count }}</span></p>      
        
    </div>


    <div class="user-div" data-url="{% url 'follow_user' chilipili.author_user.pk %}">
        {% csrf_token %}
        <button class="btn follow-button"><i class="fa fa-angle-double-up">Follow</i></button>
        <p>Followers:<span class="follow-count">{{ chilipili.author_user.follows.count }}</span></p>

    </div> 
   </div>     
    `
}

$.get('/api/chilipilis/').then(function (chilipilis) {

    for (let chilipili of chilipilis) {
        $('#chilipili-list').append(chilipiliHtml(chilipili))
    }

})




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
        if (results.followers) {
            $(parent_div).find('.follow-count').text(results.followers);
        }
    });
})
