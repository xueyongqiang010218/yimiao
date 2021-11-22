var app=new Vue({
	el:'#app',
	data:{
		host:host,
		username:'',
		name:'',
		sex:'',
		jc:'',
		userage:'',
		address:'',
		phone:'',
		list:[],
		namemsg:false,
		sexmsg:true,
		agemsg:false,
		jcmsg:true,
		addressmsg:false,
		phonemsg:false,
	},
	mounted: function () {
	    // 给 username 赋值:
	    // 获取cookie中的用户名
	    let u_json = $cookies.get('username')// 使用第三方库进行获取cookie
	    let u_str = JSON.parse(u_json) //将数据进行json反序列化
	    this.username = eval(u_str) //将uncode编码转为中文
		
		// // 获取个人信息:
		this.get_person_info()
	},
	methods:{
		on_submit:function(){
			this.checkname()
			this.checkage()
			this.checkjc()
			this.checkphone()
			this.checksex()
			this.checkdz()
			if(this.namemsg==true || this.sexmsg ==true||
			this.agemsg==true||this.jcmsg==true||this.addressmsg==true||this.phonemsg==true){
				return false
			}
			var url = this.host + '/add/';
			var data={
				name:this.name,
				sex:this.sex,
				jc:this.jc,
				age:this.userage,
				address:this.address,
				phone:this.phone				
			}
			axios.post(url, data,{
			    responseType: 'json',
			    withCredentials: true
			})
			.then(function(res){
				alert(res.data.errmsg)
				location.reload()
			})
			.catch(error => {
				console.log(error);
			})
		},
		logout:function(){
			var url = this.host + '/logout/';
			axios.get(url, {
			    responseType: 'json',
			    withCredentials: true
			})
			.then(function(){
				location.href='/login.html/'
			})
		},
		// 获取用户所有的资料
		get_person_info: function () {
		    var url = this.host + '/info/';
		    axios.get(url, {
		        responseType: 'json',
		        withCredentials: true
		    })
		    .then(response => {
		    if (response.data.code == 400) {
		         location.href = '/login.html/'
		           // return
		        }
			if(response.data.code==200){
				console.log(response.data.data)
				this.list=response.data.data
				}
		     })
			.catch(error => {
				location.href = '/login.html/'
				console.log(error);
			})
		},
		checkname:function(){
			if (this.name.length == 0){
				this.namemsg=true;
			}
			else{
				this.namemsg=false;
			}
		},
		checkage:function(){
			if(this.userage <= 0 ){
				this.agemsg=true
			}else{
				this.namemsg=false;
			}
		},
		checkdz:function(){
			if (this.address.length == 0){
				this.addressmsg=true;
			}
			else{
				this.addressmsg=false;
			}
		},
		checkphone:function(){
			if (this.phone.length == 0){
				this.phonemsg=true;
			}
			else{
				this.phonemsg=false;
			}
		},
		checksex:function(){
			if(this.sex != null){
				this.sexmsg=false
			}else{
				this.sexmsg=true
			}
		},
		checkjc:function(){
			if(this.jc != null){
				this.jcmsg=false
			}else{
				this.jcmsg=true
			}
		},
	}
})