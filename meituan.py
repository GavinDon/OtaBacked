import json
import jieba
from flask import request, Response, session
from snownlp import normal, SnowNLP, seg
from snownlp.summary import textrank
from export import app
from modles import XymTripModel


# # 判断是否已经登陆
# @app.before_request
# def before_user():
#     sess = session.get('user')
#     request.cookies.get('session')
#     if sess:
#         return '已登陆'
#     else:
#         render_template('login.html')


@app.route("/logins", methods=['POST', 'GET'])
def login():
    username = request.values['username']
    password = request.values['password']
    response = Response()
    if username == "linan":
        response.set_data("dfdasdf")
        # 存储session
        session['user'] = f'{username}'

    return response


@app.route("/sess")
def get_session():
    sessions = session.get('user')
    for i in session:
        print(i)
    return u'<address><a href="mailto:jim@rock.com">jim@rock.com</a><br><a href="tel:+13115552368">(311) 555-2368</a></address > '


@app.route('/hs')
def query_hs():
    offset = request.values['offset']
    pagesize = request.values['pageSize']
    resp = XymTripModel.query.offset(offset).limit(pagesize)
    # 评论总数
    # count = XymTripModel.query.count()
    # 进行情感分析
    # cut = jieba.cut(comment, cut_all=False)
    # print("Full Mode: " + "/ ".join(cut))  # 全模式
    lst = []
    for page in resp:
        row = ""
        seg = jieba.lcut(page.comment)
        print(seg)
        s = SnowNLP(page.comment)
        # 把一条评论进行分句
        for word in s.sentences:
            # 分句之后每段词的情感度
            single = SnowNLP(word)
            if single.sentiments <= 0.15:
                row += f"<span style='color:red'>{word}</span>"
            else:
                row += word
        finally_row = f"<p>{row}</p>"
        lst.append(finally_row)

    return json.dumps(lst, ensure_ascii=False)


@app.route("/xym")
def query_xym():
    offset = request.values['offset']
    pagesize = request.values['pageSize']

    resp = XymTripModel.query.offset(offset).limit(pagesize)
    t = normal.zh2hans(
        "随着智能手机和平板电脑的普及，相机也变得无处不在，而且分享照片也越来越简单。MOOC的明星教授说，把45分钟的讲座变成10分钟一段的视频让他们被迫“升级课程”。不是每个老师都能通过这种方式吸引一批学生，但是他们可以参考这个经验，为课堂制作自己的视频，例如实地考察录像。让整个班都出去跑一趟可能不可行，但利用视频和照片，可以把考察点“带”到课室中来。利用智能手机耳机上配备的话筒，还可以为视频配上讲解，从而高效地用多个视频介绍完一个知识点。")
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
    words = normal.filter_stop(words)
    doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    for w in keyword_rank.top_index(5):
        print(w)
    return "\'..."
