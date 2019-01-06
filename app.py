from flask import *
import hashlib, copy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/hash', methods=['POST'])
def return_hash():
    data = request.form['data']
    data2= copy.deepcopy(data)
    data = bytearray(data,"utf-8")
    algorithms = ['md5','sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256', 'blake2b', 'blake2s']
    hashes = []
    md5 = hashlib.md5(data).hexdigest()
    hashes.append(md5)
    sha1 = hashlib.sha1(data).hexdigest()
    hashes.append(sha1)
    sha224 =hashlib.sha224(data).hexdigest()
    hashes.append(sha224)
    sha256=hashlib.sha256(data).hexdigest()
    hashes.append(sha256)
    sha384=hashlib.sha384(data).hexdigest()
    hashes.append(sha384)
    sha3_224=hashlib.sha3_224(data).hexdigest()
    hashes.append(sha3_224)
    sha3_256=hashlib.sha3_256(data).hexdigest()
    hashes.append(sha3_256)
    sha3_384=hashlib.sha3_384(data).hexdigest()
    hashes.append(sha3_384)
    sha3_512=hashlib.sha3_512(data).hexdigest()
    hashes.append(sha3_512)
    sha512=hashlib.sha512(data).hexdigest()
    hashes.append(sha512)
    shake_128=hashlib.shake_128(data).hexdigest(128)
    hashes.append(shake_128)
    shake_256=hashlib.shake_256(data).hexdigest(256)
    hashes.append(shake_256)
    blake2b=hashlib.blake2b(data).hexdigest()
    hashes.append(blake2b)
    blake2s=hashlib.blake2s(data).hexdigest()
    hashes.append(blake2s)
    #print(len(hashes),len(algorithms))
    return render_template('index.html', algorithms=algorithms, hashes=hashes)
    
        
app.run(host='192.168.10.3', port='80',debug=True)
