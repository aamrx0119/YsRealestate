$( document ).ready(function() {
    $('.like-form').submit(function(e){
        e.preventDefault()
        
        // const post_id = $(this).attr('id')
        const house_id = $(this).attr('id')

        const likeText = $(`.like-btn${house_id}`).text()
        const trim = $.trim(likeText)
        const url = $(this).attr('action')
        const color = $(`.likes-color${house_id}`).attr('class')

        console.log(color)
        
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'house_id':house_id,
            },
            success: function(response) {
                if(trim === 'Unlike') {
                    $(`.like-btn${house_id}`).text('Like')
                    $(`.likes-color${house_id}`).attr({'class':`bi bi-heart-fill likes-color${house_id}`})
                    
                } else {
                    $(`.like-btn${house_id}`).text('Unlike')
                    $(`.likes-color${house_id}`).attr({'class':`bi bi-heart-fill likes-color${house_id}`})
                }

            },
            error: function(response) {
                console.log('error', response)
            }
        })

    })
});