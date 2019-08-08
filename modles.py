from export import db


class HsMeituanModel(db.Model):
    __tablename__ = 't_hs_meituan'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class HsQunarModel(db.Model):
    __tablename__ = 't_hs_qunar'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.Date)


class HsTripModel(db.Model):
    __tablename__ = 't_hs_trip'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class HsXieChengModel(db.Model):
    __tablename__ = 't_hs_xiecheng'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class XymMeituanModel(db.Model):
    __tablename__ = 't_xym_meituan'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class XymQunarModel(db.Model):
    __tablename__ = 't_xym_qunar'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class XymTripModel(db.Model):
    __tablename__ = 't_xym_trip'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class XymXieChengModel(db.Model):
    __tablename__ = 't_xym_xiecheng'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.String(225))
    userName = db.Column(db.String(225))
    comment = db.Column(db.Text)
    commentTime = db.Column(db.DATE)


class HuaShanModel(db.Model):
    __tablename__ = 't_hs'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    comment_id = db.Column(db.String(225))
    comment = db.Column(db.Text, nullable=False)
    is_neg = db.Column(db.CHAR(1))
    comment_date = db.Column(db.Date)
    media_type = db.Column(db.String(50))
    comment_url = db.Column(db.String(225))
    is_gone = db.Column(db.CHAR(1))


class XYMModel(db.Model):
    __tablename__ = 't_xym'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    comment_id = db.Column(db.String(225))
    comment = db.Column(db.Text, nullable=False)
    is_neg = db.Column(db.CHAR(1))
    comment_date = db.Column(db.Date)
    media_type = db.Column(db.String(50))
    comment_url = db.Column(db.String(225))
    is_gone = db.Column(db.CHAR(1))


class UserModel(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(50), nullable=False)
    passWord = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    telphone = db.Column(db.String(50))
    sex = db.Column(db.String(50))

    def __repr__(self):
        pass


class CollectModel(db.Model):
    __tablename__ = 't_collection'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(50), nullable=False)
    passWord = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    telPhone = db.Column(db.String(50))
    sex = db.Column(db.String(50))

    def __repr__(self):
        pass
