$(function(){
    queryCategoryData();
})

function queryAllArticle(){
    $.ajax(
        {
            url:'allArticle/',
            data:null,
            type:'get',
            dataType:'json',
            success:function(articles){
                console.log(articles);
                parseArticleData(articles);
            }
        }
    )
}

function parseArticleData(articles){

    $.each(articles, function (index, item) {

    var articleD = '<div class="articleDiv"><span class="upupnum">99999</span><div class="article">' +
    '<p class="articleTitle"><a href="#">'+ item.title +'</a> </p>' +
    '<div class="articleContent">' +
        '<div class="userImage"></div>'+ item.summery +'</div>' +
        '<div class="articleInfo"><a href="#">'+ item.uname +'</a>发布于 '+ item.createTime +'<span class="article_comment"><a href="#">评论(100)</a></span><span class="article_read"><a href="#">阅读(1900)</a></span></div></div></div>';

        $('.contentDiv').append(articleD);
    })
}

function queryCategoryData(){
     $.ajax(
            {
                url:'classficationData/',
                data:null,
                type:'get',
                dataType:'json',
                success:function(arg){
                    var ret = parseCategoryData(arg);
                    $('.menuList').append(ret);
                }
            }
        )
}

//解析分类
function  parseCategoryData(arg){
    var ret = "";
     $.each(arg, function (index, item) {
         var childData;
         var liStr = "<li class='l1'><a href=" + item.id + ">" + item.name + "</a>";
         childData  = parseChildCategoryData(item);
         liStr += childData + "</li>";
         ret += liStr;
     })
    ret = "<ul class='u1'>" + ret + "</ul>";
    return ret;
}

//解析子分类
function parseChildCategoryData(category){
    var tag = "";
    $.each(category.child, function (index, item) {
        tag += "<li class='l2'><a href=" + item.id + ">" + item.name + "</a></li>";
    })
    var ret = "";
    if(tag.length > 0){
        ret = "<ul class='u2'>" + tag + "</ul>";
    }
    return ret;
}

