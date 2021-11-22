var app=new Vue({
	el:'#app',
	data:{
		host:host,
		username:'',
		pwd:'',
		rember:'',
		nameerrmsg:false,
		pwderrmsg:false,
		
	},
	methods:{
		checkname:function(){
			if (this.username.length == 0){
				this.nameerrmsg=true;
			}
			else{
				this.nameerrmsg=false;
			}
		},
		checkpwd:function(){
			if (this.pwd.length == 0){
				this.pwderrmsg=true;
			}
			else{
				this.pwderrmsg=false;
			}
		},
		on_submit:function(){
			this.checkname()
			this.checkpwd()
			if (this.nameerrmsg == true || this.pwderrmsg == true){
				return false
			}
			var url=this.host+'/login/'
			var data={
				username:this.username,
				pwd:this.pwd,
				rember:this.rember
				}
			axios.post(url,data,{
					responseType:'json',
					withCredentials:true,
				})
			.then(function(res){
				if(res.data.code==200){
					location.href='/index.html/'
				}else{
					alert(res.data.errmsg)
				}
			})
			.catch(function(){
				alert('no')
			})
		}
	}
})