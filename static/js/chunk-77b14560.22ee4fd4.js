(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-77b14560"],{"1bf9":function(e,a,o){"use strict";o.r(a);var t=function(){var e=this,a=e.$createElement,o=e._self._c||a;return o("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:e.webTitle},expression:"{title:webTitle}"}],staticClass:"person"},[o("el-col",{attrs:{span:4}},[o("work-space")],1),o("el-col",{attrs:{span:20}}),o("div",{staticClass:"box"},[o("el-card",{staticStyle:{"background-color":"whitesmoke",border:"0px","padding-top":"80px"},attrs:{shadow:"never"}},[o("br"),o("el-row",[o("el-col",{attrs:{span:8}},[o("el-row",[o("el-avatar",{attrs:{size:80,src:e.head}})],1),o("br"),o("el-row",[e.ifChangeHeadVisible?o("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.changeHeadVisible=!0}}},[e._v("修改头像")]):e._e()],1),o("el-dialog",{attrs:{title:"修改头像",visible:e.changeHeadVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(a){e.changeHeadVisible=a}}},[o("el-form",{attrs:{model:e.form}},[o("el-form-item",{ref:"uploadElement"},[o("el-upload",{ref:"upload",class:{hide:e.hideUpload},attrs:{action:"http://127.0.0.1/users/1/",accept:"image/png,image/gif,image/jpg,image/jpeg","list-type":"picture-card","http-request":e.uploadAvatar,limit:e.limitNum,"auto-upload":!1,"on-exceed":e.handleExceed,"before-upload":e.handleBeforeUpload,"on-preview":e.handlePictureCardPreview,"on-remove":e.handleRemove,"on-change":e.imgChange,"on-success":e.handleAvatarSuccess}},[o("i",{staticClass:"el-icon-plus"})]),o("el-dialog",{attrs:{visible:e.dialogVisible},on:{"update:visible":function(a){e.dialogVisible=a}}},[o("img",{attrs:{width:"100%",src:e.dialogImageUrl,alt:""}})])],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:e.toCancel}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.uploadFile}},[e._v("确 定")])],1)],1)],1),o("el-col",{attrs:{span:4}},[o("el-form",[o("el-form-item",[o("i",{staticClass:"el-icon-user-solid"},[e._v(" 昵称")])]),o("el-form-item",[o("i",{staticClass:"el-icon-paperclip"},[e._v(" 密码")])]),o("el-form-item",[o("i",{staticClass:"el-icon-phone"},[e._v(" 手机")])]),o("el-form-item",[o("i",{staticClass:"el-icon-message"},[e._v(" 邮箱")])]),o("el-form-item",[o("i",{staticClass:"el-icon-s-flag"},[e._v(" 账号ID")])])],1)],1),o("el-col",{attrs:{span:8}},[o("el-form",[o("el-form-item",[e._v(e._s(e.name))]),o("el-form-item",[e._v("********")]),o("el-form-item",[e._v(e._s(e.phone))]),o("el-form-item",[e._v(e._s(e.email)+" ")]),o("el-form-item",[e._v(e._s(e.ID))])],1)],1),o("el-col",{attrs:{span:2}},[e.ifChangeVisible?o("el-form",[o("el-form-item",[o("el-button",{attrs:{type:"text"},on:{click:function(a){e.changeNameVisible=!0}}},[e._v("修改")]),o("el-dialog",{attrs:{title:"修改昵称",visible:e.changeNameVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(a){e.changeNameVisible=a}}},[o("el-form",{ref:"nameForm",attrs:{model:e.nameForm,rules:e.nameRules,enctype:"multipart/form-data"}},[o("el-form-item",{attrs:{prop:"newName"}},[o("el-input",{attrs:{autocomplete:"off",placeholder:"新昵称"},nativeOn:{keydown:function(a){return!a.type.indexOf("key")&&e._k(a.keyCode,"enter",13,a.key,"Enter")?null:e.changeName(a)}},model:{value:e.nameForm.newName,callback:function(a){e.$set(e.nameForm,"newName",a)},expression:"nameForm.newName"}})],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(a){e.changeNameVisible=!1}}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.changeName}},[e._v("确 定")])],1)],1)],1),o("el-form-item",[o("el-button",{attrs:{type:"text"},on:{click:function(a){e.changePasswordVisible=!0}}},[e._v("修改")]),o("el-dialog",{attrs:{title:"修改密码",visible:e.changePasswordVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(a){e.changePasswordVisible=a}}},[o("el-form",{ref:"passwordForm",attrs:{model:e.passwordForm,rules:e.passwordRules,enctype:"multipart/form-data"}},[o("el-form-item",{attrs:{prop:"newPassword"}},[o("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"新密码"},model:{value:e.passwordForm.newPassword,callback:function(a){e.$set(e.passwordForm,"newPassword",a)},expression:"passwordForm.newPassword"}})],1),o("br"),o("el-form-item",{attrs:{prop:"newPasswordAgain"}},[o("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"确认新密码"},nativeOn:{keydown:function(a){return!a.type.indexOf("key")&&e._k(a.keyCode,"enter",13,a.key,"Enter")?null:e.changePassword(a)}},model:{value:e.passwordForm.newPasswordAgain,callback:function(a){e.$set(e.passwordForm,"newPasswordAgain",a)},expression:"passwordForm.newPasswordAgain"}})],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(a){e.changePasswordVisible=!1}}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.changePassword}},[e._v("确 定")])],1)],1)],1),o("el-form-item",[o("el-button",{attrs:{type:"text"},on:{click:function(a){e.changePhoneVisible=!0}}},[e._v("修改")]),o("el-dialog",{attrs:{title:"修改手机号",visible:e.changePhoneVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(a){e.changePhoneVisible=a}}},[o("el-form",{ref:"phoneForm",attrs:{model:e.phoneForm,rules:e.phoneRules,enctype:"multipart/form-data"}},[o("el-form-item",[o("el-input",{attrs:{type:"tel",autocomplete:"off",placeholder:"新手机号"},nativeOn:{keydown:function(a){return!a.type.indexOf("key")&&e._k(a.keyCode,"enter",13,a.key,"Enter")?null:e.changePhone(a)}},model:{value:e.phoneForm.newPhone,callback:function(a){e.$set(e.phoneForm,"newPhone",a)},expression:"phoneForm.newPhone"}})],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(a){e.changePhoneVisible=!1}}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.changePhone}},[e._v("确 定")])],1)],1)],1),o("el-form-item",[o("el-button",{attrs:{type:"text"},on:{click:function(a){e.changeEmailVisible=!0}}},[e._v("修改")]),o("el-dialog",{attrs:{title:"修改邮箱",visible:e.changeEmailVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(a){e.changeEmailVisible=a}}},[o("el-form",{ref:"emailForm",attrs:{model:e.emailForm,rules:e.emailRules,enctype:"multipart/form-data"}},[o("el-form-item",[o("el-input",{attrs:{type:"email",autocomplete:"off",placeholder:"新邮箱"},nativeOn:{keydown:function(a){return!a.type.indexOf("key")&&e._k(a.keyCode,"enter",13,a.key,"Enter")?null:e.changeEmail(a)}},model:{value:e.emailForm.newEmail,callback:function(a){e.$set(e.emailForm,"newEmail",a)},expression:"emailForm.newEmail"}})],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(a){e.changeEmailVisible=!1}}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.changeEmail}},[e._v("确 定")])],1)],1)],1)],1):e._e()],1)],1)],1)],1)],1)},s=[],i=(o("053b"),o("365c")),n=o("4ec3"),l={data:function(){var e=this,a=function(a,o,t){""===o?t(new Error("请再次输入密码")):o!==e.passwordForm.newPassword?t(new Error("两次密码输入不一致")):t()};return{webTitle:"个人主页",name:"whisper",password:"123123",phone:"18538947201",email:"1214960505@qq.com",ID:"18373154",head:"https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",uploadurl:"http://127.0.0.1:8000/users/",hideUpload:!1,dialogImageUrl:"",dialogVisible:!1,limitNum:1,form:{},dialogVisible2:!1,ifChangeVisible:!0,ifChangeHeadVisible:!0,changeHeadVisible:!1,changePasswordVisible:!1,changePhoneVisible:!1,changeEmailVisible:!1,changeNameVisible:!1,headForm:{newHead:""},passwordForm:{newPassword:"",newPasswordAgain:""},passwordRules:{newPassword:[{required:!0,message:"请输入新密码",trigger:"blur"},{min:4,max:18,message:"密码至少四位",trigger:"blur"}],newPasswordAgain:[{required:!0,message:"两次输入密码必须一致",trigger:"blur",validator:a}]},phoneForm:{newPhone:""},phoneRules:{newPhone:[{required:!0,message:"请输入新手机号",trigger:"blur"}]},emailForm:{newEmail:""},emailRules:{newEmail:[{required:!0,message:"请输入新邮箱",trigger:"blur"}]},nameForm:{newName:""},nameRules:{newName:[{required:!0,message:"请输入新昵称",trigger:"blur"}]}}},methods:{getPersonInfo:function(e){var a=this;Object(n["B"])(e).then((function(e){200===e.status?(console.log(e),a.name=e.data.username,a.phone=e.data.mobile,""===e.data.email?a.email="未填写":a.email=e.data.email,a.password=e.data.password,a.ID=e.data.id,a.head=e.data.head,a.webTitle=a.name+"的个人主页"):a.$message({message:"获取信息失败"+e.message,type:"error"})})).catch((function(e){console.log(e.response)}))},getOtherInfo:function(e){var a=this;Object(n["A"])(e).then((function(e){200===e.status?(console.log(e),a.name=e.data.username,a.phone=e.data.mobile,""===e.data.email?a.email="未填写":a.email=e.data.email,a.password=e.data.password,a.ID=e.data.id,a.head=e.data.head,a.webTitle=a.name+"的个人主页"):a.$message({message:"获取信息失败"+e.message,type:"error"})})).catch((function(e){console.log(e.response)}))},changeName:function(){var e=this;this.$refs.nameForm.validate((function(a){if(a){var o=i["a"];o.patch("/users/"+localStorage.userId+"/",{username:e.nameForm.newName}).then((function(a){200===a.status?(console.log(a),console.log(localStorage.token),e.name=e.nameForm.newName,e.nameForm.newName="",e.$message({message:"修改昵称成功",type:"info"}),e.$router.push({name:"Login"})):e.$message({message:"修改昵称失败",type:"error"})})).catch((function(e){console.log(e.response)})),e.changeNameVisible=!1,e.$refs.nameForm.resetFields()}}))},changePassword:function(){var e=this;this.$refs.passwordForm.validate((function(a){if(a){var o=i["a"];o.patch("/users/"+localStorage.userId+"/",{password:e.passwordForm.newPassword}).then((function(a){200===a.status?(console.log(a),console.log(localStorage.token),e.password=e.passwordForm.newPassword,e.passwordForm.newPassword="",e.passwordForm.newPasswordAgain="",e.$message({message:"修改密码成功",type:"info"})):e.$message({message:"修改密码失败",type:"error"})})).catch((function(e){console.log(e.response)})),e.changePasswordVisible=!1,e.$refs.passwordForm.resetFields()}}))},changePhone:function(){var e=this;this.$refs.phoneForm.validate((function(a){if(a){var o=i["a"];o.patch("/users/"+localStorage.userId+"/",{mobile:e.phoneForm.newPhone}).then((function(a){200===a.status?(console.log(a),console.log(localStorage.token),e.phone=e.phoneForm.newPhone,e.phoneForm.newPhone="",e.$message({message:"修改手机号码成功",type:"info"})):e.$message({message:"修改手机号码失败",type:"error"})})).catch((function(e){console.log(e.response)})),e.changePhoneVisible=!1,e.$refs.phoneForm.resetFields()}}))},changeEmail:function(){var e=this;this.$refs.emailForm.validate((function(a){if(a){var o=i["a"];o.patch("/users/"+localStorage.userId+"/",{email:e.emailForm.newEmail}).then((function(a){200===a.status?(console.log(a),console.log(localStorage.token),e.email=e.emailForm.newEmail,e.emailForm.newEmail="",e.$message({message:"修改邮箱成功",type:"info"})):e.$message({message:"修改邮箱失败",type:"error"})})).catch((function(e){console.log(e.response)})),e.changeEmailVisible=!1,e.$refs.emailForm.resetFields()}}))},handleBeforeUpload:function(e){"image/png"!==e.type&&"image/gif"!==e.type&&"image/jpg"!==e.type&&"image/jpeg"!==e.type&&this.$message({type:"error",message:"请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片"});var a=e.size/1024/1024/2;a>2&&this.$message({type:"error",message:"图片大小必须小于2M"}),("image/png"===e.type||"image/gif"===e.type||"image/jpg"===e.type||"image/jpeg"===e.type)&&a<=2&&(this.headFile=e,console.log("headfile:"+this.headFile))},uploadAvatar:function(){var e=this,a=new FormData;a.append("head",this.headFile),console.log(a.get("picFile"));var o=i["a"];o.patch("/users/1/",a).then((function(a){console.log(a),200===a.status?(console.log(a),e.head=a.data.head,e.headForm.newHead="",localStorage.head=e.head,e.$addStorageEvent("head",e.head),e.$message({message:"修改头像成功",type:"info"}),e.getPersonInfo()):e.$message({message:"修改头像失败",type:"error"})})).catch((function(e){console.log(e.response)})),this.changeHeadVisible=!1,this.$refs.headForm.resetFields(),this.headForm.newHead=""},handleExceed:function(e,a){this.hideUpload=a.length>=this.limitNum},handleRemove:function(e,a){this.hideUpload=a.length>=this.limitNum},handlePictureCardPreview:function(e){this.dialogImageUrl=e.url,this.dialogVisible=!0},uploadFile:function(){this.$refs.upload.submit()},imgChange:function(e,a){this.hideUpload=a.length>=this.limitNum,a&&this.$refs.uploadElement.clearValidate()},handleAvatarSuccess:function(e){window.console.log(e)},toCancel:function(){this.changeHeadVisible=!1}},mounted:function(){console.log(this.$route.params.personId),this.ID=this.$route.params.personId,console.log("users",this.ID+""===localStorage.userId+""),this.ID+""===localStorage.userId+""?(this.ifChangeVisible=!0,this.ifChangeHeadVisible=!0,this.getPersonInfo(this.$route.params.personId)):(this.ifChangeVisible=!1,this.ifChangeHeadVisible=!1,this.getOtherInfo(this.$route.params.personId))},watch:{head:{handler:function(e,a){e!==a&&this.getPersonInfo(this.ID)},immediate:!0}}},r=l,m=(o("4494"),o("2877")),c=Object(m["a"])(r,t,s,!1,null,null,null);a["default"]=c.exports},4494:function(e,a,o){"use strict";var t=o("ee28"),s=o.n(t);s.a},ee28:function(e,a,o){}}]);
//# sourceMappingURL=chunk-77b14560.22ee4fd4.js.map