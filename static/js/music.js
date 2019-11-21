


$(document).ready(function () {
        // ajax加载音乐
    var page = 0
    $("#music").click(function () {

        $(window).scroll(function () {
              if($(window).scrollTop()==($(document).height()-$(window).height()))
              {
                  $.ajax({
            url: "/music/" + page,
            success: function (result) {
                page += 5
                var musUrl = JSON.parse(result)
                var contain = ''
                console.log(musUrl)
                for (var el in musUrl) {
                    console.log(musUrl[el].musAddr)
                    if (musUrl[el].user_com_name){
                    contain += `<div class='well' style="text-align: center">
                                        <div class="head">
                                        
                                        <img  class="img-circle" src="${musUrl[el].user_icon}" style="width: 100px;height: 100px">
                                        </div>
                                        <div class="user_name">${musUrl[el].user_com_name}
                                        </div>
                                        <div>${musUrl[el].music_title}</div>
                                        <audio controls>
                                            <source src="${musUrl[el].musAddr}"></audio>
                                        <div class="operation">
                                            <div class="comment_music" key="${musUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${musUrl[el].id}" type="music" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${musUrl[el].ct}</button></div>
                                        </div>
                                </div>`
                    }else{
                                            contain += `<div class='well' style="text-align: center">
                                        <div class="head">
                                        <img  class="img-circle" src="${musUrl[el].admin_icon}" style="width: 100px;height: 100px">
                                        
                                        </div>
                                        <div class="user_name">${musUrl[el].admin_com_name}
                                        </div>
                                        <div>
                                        ${musUrl[el].music_title}</div>
                                        <audio controls>
                                            <source src="${musUrl[el].musAddr}"></audio>
                                        <div class="operation">
                                            <div class="comment_music" key="${musUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${musUrl[el].id}" type="music" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${music[el].ct}</button></div>
                                        </div>
                                </div>`
                    }
                }
                $(".music").append(contain);
            }
        })
              }
        })

    })

            // 点击评论
        $(document).on('click','.comment_music',function (e) {
            console.log(e)
            e.stopPropagation()
            var that=$(this);
            console.log(that.attr('key'))
            // window.location.href ='/comment/'+that.attr('key')原窗口跳转
            window.open('/comment_music/'+that.attr('key')) //新窗口打开
        })
})