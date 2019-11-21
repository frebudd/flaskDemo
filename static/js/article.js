


$(document).ready(function(){

    var articleId=0
    var page_article=0
        $("#article").click(function () {



          // var page_article=Math.ceil(Math.random()*200)
        $(window).scroll(function () {
            if($(window).scrollTop()==($(document).height()-$(window).height()))//判断右边滑动条是否滑到最下
            {
                $.ajax({
                    url:"/article/"+page_article,
                    success:function(result){
                        page_article=page_article+5
                        var articleUrl=JSON.parse(result)
                        console.log(articleUrl)
                        var contain=''
                        for(var el in articleUrl) {
                            if (articleUrl[el].admin_icon) {
                                contain += `<div class='well' style="text-align: center">
                                        <div class="head">
                                        <img  class="img-circle" src="${articleUrl[el].admin_icon}" style="width: 100px;height: 100px">
                                        </div>
                                        <div class="user_name">${articleUrl[el].com_name}</div>
                                        <h3 id="article_title">${articleUrl[el].art_cont}</h3>
                                        <p id="article_cont">${articleUrl[el].art_addr}</p>
                                         <div class="operation" style="display: flex;justify-content: space-between">
                                            <div class="comment_article" key="${articleUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${articleUrl[el].id}" type="article" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${articleUrl[el].ct}</button></div>
                                        </div>
                                        </div>
                                </div>`
                            }else {
                                 contain += `<div class='well' style="text-align: center">
                                        <div class="head">
                                        <img  class="img-circle" src="${articleUrl[el].user_icon}" style="width: 100px;height: 100px">
                                        </div>
                                        <div class="user_name">${articleUrl[el].user_com_name}</div>
                                        <h3 id="article_title">${articleUrl[el].art_cont}</h3>
                                        <p id="article_cont">${articleUrl[el].art_addr}</p>
                                         <div class="operation" style="display: flex;justify-content: space-between">
                                            <div class="comment_article" key="${articleUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${articleUrl[el].id}" type="article" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${articleUrl[el].ct}</button></div>
                                        </div>
                                        </div>`
                            }
                        }
                    $(".article").append(contain);
                    }
                 }
                )
            }
        })
        })
        // 点击评论

        $(document).on('click','.comment_article',function (e) {
            console.log(e)
            e.stopPropagation()
            var that=$(this);
            console.log(that.attr('key'))
            window.open('/comment_article/'+that.attr('key')) //新窗口打开
        })
        // 文章截断
        $(document).on('click','#article_cont',function () {
            if ($(this).css("overflow")=="hidden"){
                $(this).css("overflow","auto");
                $(this).css("height","auto");
            }
            else {
                $(this).css("overflow","hidden");
                $(this).css("height","15em");
            }

        })
})