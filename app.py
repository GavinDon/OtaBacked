from functools import wraps

from flask import render_template, request, Response, session
from snownlp import SnowNLP
from export import app, db
import modles
from modles import HuaShanModel, XYMModel
import custom_response
import datetime

from expands import isNotEmpty, now_date

''''
判断是否登陆
'''


def judge_login(func):
    @wraps(func)
    def check_login():
        if not session.get('user'):
            return custom_response.UnauthorizedResponse()
        return func()

    return check_login


@app.route("/")
def index():
    print(__name__)
    return render_template('login.html')


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'), 404


@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = Response()
    # 存储session
    session['user'] = f'{username}'
    # 必须设置否则PERMANENT_SESSION_LIFETIME无效 默认session保存31天
    session.permanent = True

    return custom_response.SuccessResponse(data="ada")


@app.route('/meit/hs')
def query_meituan_hs():
    # offset = request.values.get('offset')
    # pagesize = request.values.get('pageSize')
    # dir(SnowNLP)
    # resp = modles.HsMeituanModel.query.offset(offset).limit(pagesize)
    # total = modles.HsMeituanModel.query.count()
    # # 评论总数
    # # count = XymTripModel.query.count()
    # # 进行情感分析
    # # cut = jieba.cut(comment, cut_all=False)
    # # print("Full Mode: " + "/ ".join(cut))  # 全模式
    # lst = []
    # print(dir(resp))
    # for page in resp:
    #     row = ""
    #     # keywords = analyse.textrank(page.comment)
    #     # for k in keywords:
    #     #     print(f'{k}//')
    #     # seg = jieba.lcut(page.comment)
    #     # print(seg)
    #     s = SnowNLP(page.comment)
    #     # 把一条评论进行分句
    #     for word in s.sentences:
    #         # 分句之后每段词的情感度
    #         single = SnowNLP(word)
    #         if single.sentiments <= 0.15:
    #             row += f"<span style='color:red'>{word}</span>"
    #         else:
    #             row += word
    #     finally_row = f"<p>{row}</p>"
    #     lst.append(finally_row)
    data = comment_process(modles.HsMeituanModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/meit/xym')
def query_meituan_xym():
    data = comment_process(modles.XymMeituanModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/qunar/hs')
def query_qunar_hs():
    data = comment_process(modles.HsQunarModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/qunar/xym')
def query_qunar_xym():
    data = comment_process(modles.XymQunarModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/trip/hs')
def query_trip_hs():
    data = comment_process(modles.HsTripModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/trip/xym')
def query_trip_xym():
    data = comment_process(modles.XymTripModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/xiec/hs')
def query_xiec_hs():
    data = comment_process(modles.HsXieChengModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/xiec/xym')
def query_xiec_xym():
    data = comment_process(modles.XymXieChengModel.query)
    return custom_response.SuccessResponse(data=data[0], total=data[1])


@app.route('/scenic/hs')
def resp_hs():
    resp = resp_process(HuaShanModel)
    return custom_response.SuccessResponse(data=resp[0], total=resp[1])


@app.route('/scenic/xym')
def resp_xym():
    resp = resp_process(XYMModel)
    return custom_response.SuccessResponse(data=resp[0], total=resp[1])


"""
:parameter scenic景点
0华山
1西岳庙

"""


@app.route('/delete')
def del_comment_hs():
    del_id = request.values.get('id')
    scenic = request.values.get('scenic')
    if isNotEmpty(del_id) and isNotEmpty(scenic):
        if scenic == '0':
            HuaShanModel.query.filter_by(id=int(del_id)).update(dict(is_gone='1'))
        elif scenic == '1':
            XYMModel.query.filter_by(id=int(del_id)).update(dict(is_gone='1'))
        db.session.commit()
        return custom_response.SucNoticeResponse('删除成功')
    else:
        return custom_response.ErrorResponse('参数传递错误')


def resp_process(model):
    offset = request.values.get('offset')
    pagesize = request.values.get('pageSize')
    negative = request.values.get('type')
    media_type = request.values.get('mediaType')
    key = request.values.get('key')
    start_date = request.values.get('startDate')
    end_date = request.values.get('endDate')
    if pagesize is None:
        pagesize = 10
    if offset is None:
        offset = 10
    filters = [model.is_gone == '0']
    if isNotEmpty(key):
        filters.append(model.key == key)
    if isNotEmpty(negative):
        filters.append(model.is_neg == negative)
    if isNotEmpty(media_type):
        filters.append(model.media_type == media_type)
    if isNotEmpty(start_date):
        if start_date > end_date:
            return custom_response.ErrorResponse(error_msg='请选则正确的起始时间..')
        else:
            if isNotEmpty(end_date):
                filters.append(model.comment_date.between(start_date, end_date))
            else:
                filters.append(model.comment_date.between(start_date, now_date()[1]))

    resp = model.query.filter(*filters).offset(
        offset).limit(pagesize)

    lst = []
    for page in resp:
        resp_dict = dict()
        resp_dict['id'] = page.id
        date = page.comment_date
        if date is None:
            resp_dict['date'] = ''
        else:
            resp_dict['date'] = datetime.datetime.strftime(date, '%Y-%m-%d')
        resp_dict['comment'] = page.comment
        resp_dict['commentUrl'] = page.comment_url
        resp_dict['commentId'] = page.comment_id
        resp_dict['mediaType'] = page.media_type
        resp_dict['negative'] = page.is_neg
        lst.append(resp_dict)
    return lst, resp.count()


# 获取评论列表
def comment_process(model):
    offset = request.values.get('offset')
    pagesize = request.values.get('pageSize')
    resp = model.offset(offset).limit(pagesize)
    total = model.count()
    lst = []
    for page in resp:
        resp_dict = dict()
        row = ""
        # 是否是消极
        is_neg = False
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
        resp_dict['id'] = page.id
        date = page.commentTime
        if date is None:
            resp_dict['date'] = ''
        else:
            resp_dict['date'] = datetime.datetime.strftime(date, '%Y-%m-%d')
        resp_dict['comment'] = finally_row
        lst.append(resp_dict)
    return lst, total


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
