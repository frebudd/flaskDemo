


$(document).ready(function(){
 // 点击图片按钮加载图片
    var page = 0
        $("#photo").click(function () {
                    //滑动ajax加载图片
          // var page=Math.ceil(Math.random()*200)

        $(window).scroll(function () {
            if($(window).scrollTop()==($(document).height()-$(window).height()))//判断右边滑动条是否滑到最下
            {
                $.ajax({
                    url:"/photo/"+page,
                    success:function(result){
                        console.log(page)
                        page=page+5
                        var picUrl=JSON.parse(result)
                        console.log(picUrl)
                        var contain=''
                        for(var el in picUrl){
                            if (picUrl[el].user_icon){
                                contain+=`<div class='well' style="text-align: center">
                                        <div class="head">
                                        <img  class="img-circle" src="${picUrl[el].user_icon}" style="width: 100px;height: 100px">
</div>
                                        <div class="user_name">${picUrl[el].com_name}</div>
                                        <img src="${picUrl[el].phoAddr}" class="mybig" style="width:100%;display: none">
                                        <img src="${picUrl[el].phoAddr}" class="mysmall" style="width:30%;">
                                        <div class="operation" style="display: flex;justify-content: space-between">
                                            <div class="comment" key="${picUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${picUrl[el].id}" type="pic" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${picUrl[el].ct}</button></div>
                                        </div>
                                </div>`
                            }else {
                                contain+=`<div class='well' style="text-align: center">
                                        <div class="head">
                                        <img  class="img-circle" src="${picUrl[el].admin_icon}" style="width: 100px;height: 100px">
</div>
                                        <div class="user_name">${picUrl[el].admin_com_name}</div>
                                        <img src="${picUrl[el].phoAddr}" class="mybig" style="width:100%;display: none">
                                        <img src="${picUrl[el].phoAddr}" class="mysmall" style="width:30%;">
                                        <div class="operation" style="display: flex;justify-content: space-between">
                                            <div class="comment" key="${picUrl[el].id}"  style="width: 50%">
                                            <button class="btn" style="width: 100%">comment</button></div>
                                            <div class="praise" key="${picUrl[el].id}" type="pic" style="width: 50%">
                                            <button class="btn" style="width: 100%" >good   ${picUrl[el].ct}</button></div>
                                        </div>
                                </div>`
                            }

                        }
                        $("#pho").append(contain);
                    }
                 }
                )
            }
        })
        })
        // 点击放大缩小图片
        $(document).on('click','.well',function () {
                            var that=$(this);
                            // console.log(that)
                            that.find('.mysmall').toggle();
                            that.find('.mybig').toggle();
                            // that.siblings('.pic').toggle()

        })

        // 点击评论
        $(document).on('click','.comment',function (e) {
            console.log(e)
            e.stopPropagation()
            var that=$(this);
            console.log(that.attr('key'))
            // window.location.href ='/comment/'+that.attr('key')原窗口跳转
            window.open('/comment_pic/'+that.attr('key')) //新窗口打开
        })
})