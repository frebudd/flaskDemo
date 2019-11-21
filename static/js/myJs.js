$(document).ready(function () {
    // 点击显示隐藏div
    $("#navPic").click(function () {
        $(".photo").css("display", "block")
        $(".article").css("display", "none")
        $(".music").css("display", "none")
    })
    $("#navMus").click(function () {
        $(".photo").css("display", "none")
        $(".article").css("display", "none")
        $(".music").css("display", "block")
    })
    $("#navArt").click(function () {
        $(".photo").css("display", "none")
        $(".article").css("display", "block")
        $(".music").css("display", "none")
    })


    // 用户点赞
    $(document).on('click', '.praise', function (e) {
        // console.log(e)
        e.stopPropagation()
        var that = $(this);
        console.log(that.attr('key'))
        console.log(that.attr('type'))
        $.ajax({
            url: '/praise',
            data: JSON.stringify({
                "objId": that.attr('key'),
                "obj_type": that.attr('type')
            }),
            type: 'POST',
            success: function (result) {
                console.log(result)
                var praise = JSON.parse(result)
                that.find('.btn').text("good" + praise[0].ct)
            }
        })

    })
    // 轮播图时间
    $("#myCarousel").carousel({
        interval: 2000
    })

    // 轮播图内容
    function carousel(){
        $.ajax({
            url:'/carousel',
            success:function (result) {
                console.log(result)
                var carousel_cont=JSON.parse(result)
                $("#item_one").append(carousel_cont.item_one)
                $("#item_two").append(carousel_cont.item_two)
                $("#item_three").append(carousel_cont.item_three)
            }
        })
    }
    carousel()

})

