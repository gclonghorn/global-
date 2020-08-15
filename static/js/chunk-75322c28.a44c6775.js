(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-75322c28"],{"2cfd":function(e,t,s){"use strict";var r=s("e314"),o=s.n(r);o.a},"73cf":function(e,t,s){"use strict";s.r(t);var r=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"basic"},[s("div",{staticStyle:{display:"flex","justify-content":"center","margin-top":"50px"}},[s("el-card",{staticStyle:{width:"400px"},attrs:{shadow:"hover"}},[s("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[s("span",{staticStyle:{"margin-left":"45%"}},[e._v("注 册")])]),s("el-form",{ref:"infoForm",attrs:{size:"small",model:e.user,rules:e.rules,"validate-on-rule-change":!0,"label-position":e.right}},[s("el-form-item",{attrs:{label:"手机号",prop:"phone"}},[s("el-input",{staticStyle:{width:"78%",float:"right"},attrs:{type:"tel","show-word-limit":""},model:{value:e.user.phone,callback:function(t){e.$set(e.user,"phone",t)},expression:"user.phone"}})],1),s("el-form-item",{attrs:{label:"验证码",prop:"code"}},[s("el-input",{staticStyle:{width:"49%",float:"left","margin-left":"5%"},attrs:{"show-word-limit":""},model:{value:e.user.code,callback:function(t){e.$set(e.user,"code",t)},expression:"user.code"}}),s("el-button",{staticStyle:{float:"right",padding:"10px","line-height":"10px",width:"100px"},attrs:{disabled:e.codeButton},on:{click:e.getCode}},[e._v(e._s(e.content))])],1),s("el-form-item",{attrs:{label:"昵称",prop:"name"}},[s("el-input",{staticStyle:{width:"78%",float:"right"},attrs:{"show-word-limit":""},model:{value:e.user.name,callback:function(t){e.$set(e.user,"name",t)},expression:"user.name"}})],1),s("el-form-item",{attrs:{label:"密码",prop:"password1"}},[s("el-input",{staticStyle:{width:"78%",float:"right"},attrs:{type:"password",maxlength:"20","show-word-limit":""},model:{value:e.user.password1,callback:function(t){e.$set(e.user,"password1",t)},expression:"user.password1"}})],1),s("el-form-item",{attrs:{label:"密码确认",prop:"password2"}},[s("el-input",{staticStyle:{width:"78%",float:"right"},attrs:{placeholder:"请再次输入密码",type:"password",maxlength:"20","show-word-limit":""},model:{value:e.user.password2,callback:function(t){e.$set(e.user,"password2",t)},expression:"user.password2"}})],1),s("el-form-item",[s("el-button",{staticStyle:{width:"100%"},attrs:{type:"primary"},on:{click:e.doRegister}},[e._v("注册")]),s("tr",[s("el-link",{staticStyle:{float:"left"},attrs:{type:"primary",underline:!1},on:{click:e.toLogin}},[e._v("已有账号？点我登录")])],1)],1)],1)],1)],1)])},o=[],a=(s("b0c0"),s("4ec3")),i={data:function(){var e=this,t=function(t,s,r){""===s?r(new Error("请再次输入密码")):s!==e.user.password1?r(new Error("两次密码输入不一致")):r()};return{content:"发送验证码",time:60,codeButton:!1,user:{phone:"",code:"",name:"",password1:"",password2:""},rules:{phone:[{required:!0,message:"手机号不能为空",trigger:"blur"},{min:11,max:11,message:"请输入11位手机号",trigger:"blur"}],code:[{required:!0,message:"验证码不能为空",trigger:"blur"}],name:[{required:!0,message:"用户名不能为空",trigger:"blur"}],password1:[{required:!0,message:"密码不能为空",trigger:"blur"},{min:4,max:18,message:"密码至少4位",trigger:"blur"}],password2:[{required:!0,message:"两次输入密码必须一致",trigger:"blur",validator:t}]}}},methods:{toLogin:function(){this.$router.push({path:"/Login"})},getCode:function(){var e=this;if(!this.codeButton){this.codeButton=!0,this.codeButton=this.time+"s后重新发送";var t=window.setInterval((function(){e.time--,e.content=e.time+"s后重新发送",e.time<0&&(window.clearInterval(t),e.content="重新发送验证码",e.time=60,e.codeButton=!1)}),1e3);Object(a["c"])(this.phone).then((function(t){200===t.status?(console.log(t),e.$message({message:"验证码发送成功",type:"success"})):400===t.status&&e.$message({message:"验证码发送失败",type:"error"})})).catch((function(t){e.$message({message:t.data[0],type:"danger"})}))}},doRegister:function(){var e=this;this.$refs.infoForm.validate((function(t){t&&Object(a["d"])(e.user.name,e.user.password1,e.user.password2,e.user.phone,e.user.code).then((function(t){console.log(t),e.$message({message:"注册成功",type:"success"}),400===t.status&&e.$message({message:"昵称或手机号已被使用 或验证码输入错误",type:"error"}),e.$router.push({path:"/Login"})})).catch((function(e){console.log("error"+e)}))}))}}},n=i,l=(s("2cfd"),s("2877")),c=Object(l["a"])(n,r,o,!1,null,null,null);t["default"]=c.exports},e314:function(e,t,s){}}]);
//# sourceMappingURL=chunk-75322c28.a44c6775.js.map