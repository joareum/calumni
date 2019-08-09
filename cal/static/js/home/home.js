var select2 = document.getElementById('b')
var a = document.getElementById('big')

a.addEventListener(
    'change',function() {
        if (this.value === 'a') {
        var opt1 = document.createElement('option')
        var opt2 = document.createElement('option')
        opt1.value = 'x'
        opt1.text = '해외'
        opt2.value = 'y'
        opt2.text = '국내'
        select2.add(opt1, null)
        select2.add(opt2, null)
        } 
        
        else if (this.value === 'b') {
        select_flush(select2.length)
        var opt3 = document.createElement('option')
        var opt4 = document.createElement('option')
        opt3.value = 'official'
        opt3.text = '공기업'
        opt4.value = 'private'
        opt4.text = '사기업'
        select2.add(opt3, null)
        select2.add(opt4, null)
        }

        else if (this.value === 'c') {
            select_flush(select2.length)
            var opt5 = document.createElement('option')
            var opt6 = document.createElement('option')
            var opt7 = document.createElement('option')
            opt5.value = 'admin'
            opt5.text = '행정,세무,사서'
            opt6.value = 'technic'
            opt6.text = '기술직'
            opt7.value = 'nurse'
            opt7.text = '간호, 보건'
            select2.add(opt5, null)
            select2.add(opt6, null)
            select2.add(opt7, null)
            }

            else if (this.value === 'd') {
                select_flush(select2.length)
                var opt8 = document.createElement('option')
                var opt9 = document.createElement('option')
                var opt10 = document.createElement('option')
                var opt11 = document.createElement('option')
                opt8.value = 'service'
                opt8.text = '서비스'
                opt9.value = 'distribution'
                opt9.text = '유통'
                opt10.value = 'make'
                opt10.text = '제조'
                opt11.value = 'etc'
                opt11.text = 'etc'
                select2.add(opt8, null)
                select2.add(opt9, null)
                select2.add(opt10, null)
                select2.add(opt11, null)
                }
  },
  false
)

function select_flush(count) {
  // var temp = select2.length
  // console.log(temp)
  for (var k = 0; k < count; k++) {
    select2.options[0] = null
  }
}