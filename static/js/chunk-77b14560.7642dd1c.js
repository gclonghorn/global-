(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-77b14560"],{"1bf9":function(e,o,t){"use strict";t.r(o);var a=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",{staticClass:"person"},[t("el-col",{attrs:{span:4}},[t("work-space")],1),t("el-col",{attrs:{span:20}}),t("div",{staticClass:"box"},[t("el-card",{staticStyle:{"background-color":"whitesmoke",border:"0px","padding-top":"80px"},attrs:{shadow:"never"}},[t("br"),t("el-row",[t("el-col",{attrs:{span:8}},[t("el-row",[t("el-avatar",{attrs:{size:80,src:e.head}})],1),t("br"),t("el-row",[t("el-button",{attrs:{type:"text",icon:"el-icon-edit"}},[e._v("修改头像")])],1)],1),t("el-col",{attrs:{span:4}},[t("el-form",[t("el-form-item",[t("i",{staticClass:"el-icon-user-solid"},[e._v(" 昵称")])]),t("el-form-item",[t("i",{staticClass:"el-icon-paperclip"},[e._v(" 密码")])]),t("el-form-item",[t("i",{staticClass:"el-icon-phone"},[e._v(" 手机")])]),t("el-form-item",[t("i",{staticClass:"el-icon-message"},[e._v(" 邮箱")])]),t("el-form-item",[t("i",{staticClass:"el-icon-s-flag"},[e._v(" 账号ID")])])],1)],1),t("el-col",{attrs:{span:8}},[t("el-form",[t("el-form-item",[e._v(e._s(e.name))]),t("el-form-item",[e._v("********")]),t("el-form-item",[e._v(e._s(e.phone))]),t("el-form-item",[e._v(e._s(e.email)+" ")]),t("el-form-item",[e._v(e._s(e.ID))])],1)],1),t("el-col",{attrs:{span:2}},[t("el-form",[t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changeNameVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改昵称",visible:e.changeNameVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changeNameVisible=o}}},[t("el-form",{ref:"nameForm",attrs:{model:e.nameForm,rules:e.nameRules,enctype:"multipart/form-data"}},[t("el-form-item",{attrs:{prop:"newName"}},[t("el-input",{attrs:{autocomplete:"off",placeholder:"新昵称"},model:{value:e.nameForm.newName,callback:function(o){e.$set(e.nameForm,"newName",o)},expression:"nameForm.newName"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changeNameVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:e.changeName}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changePasswordVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改密码",visible:e.changePasswordVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changePasswordVisible=o}}},[t("el-form",{attrs:{model:e.passwordForm}},[t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"当前密码"},model:{value:e.passwordForm.currentPassword,callback:function(o){e.$set(e.passwordForm,"currentPassword",o)},expression:"passwordForm.currentPassword"}})],1),t("br"),t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"新密码"},model:{value:e.passwordForm.newPassword,callback:function(o){e.$set(e.passwordForm,"newPassword",o)},expression:"passwordForm.newPassword"}})],1),t("br"),t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"确认新密码"},model:{value:e.passwordForm.newPasswordAgain,callback:function(o){e.$set(e.passwordForm,"newPasswordAgain",o)},expression:"passwordForm.newPasswordAgain"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changePasswordVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:function(o){e.changePasswordVisible=!1}}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changePhoneVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改手机号",visible:e.changePhoneVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changePhoneVisible=o}}},[t("el-form",{ref:"phoneForm",attrs:{model:e.phoneForm,rules:e.phoneRules,enctype:"multipart/form-data"}},[t("el-form-item",[t("el-input",{attrs:{type:"tel",autocomplete:"off",placeholder:"新手机号"},model:{value:e.phoneForm.newPhone,callback:function(o){e.$set(e.phoneForm,"newPhone",o)},expression:"phoneForm.newPhone"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changePhoneVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:e.changePhone}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changeEmailVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改邮箱",visible:e.changeEmailVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changeEmailVisible=o}}},[t("el-form",{ref:"emailForm",attrs:{model:e.emailForm,rules:e.emailRules,enctype:"multipart/form-data"}},[t("el-form-item",[t("el-input",{attrs:{type:"tel",autocomplete:"off",placeholder:"新邮箱"},model:{value:e.emailForm.newEmail,callback:function(o){e.$set(e.emailForm,"newEmail",o)},expression:"emailForm.newEmail"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changeEmailVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:e.changeEmail}},[e._v("确 定")])],1)],1)],1)],1)],1)],1)],1)],1)],1)},s=[],n=(t("b0c0"),t("365c")),l=t("4ec3"),r={data:function(){return{name:"whisper",password:"123123",phone:"18538947201",email:"1214960505@qq.com",ID:"18373154",head:"https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",changePasswordVisible:!1,changePhoneVisible:!1,changeEmailVisible:!1,changeNameVisible:!1,passwordForm:{currentPassword:"",newPassword:"",newPasswordAgain:""},phoneForm:{newPhone:""},phoneRules:{newPhone:[{required:!0,message:"请输入新手机号",trigger:"blur"}]},emailForm:{newEmail:""},emailRules:{newEmail:[{required:!0,message:"请输入新邮箱",trigger:"blur"}]},nameForm:{newName:""},nameRules:{newName:[{required:!0,message:"请输入新昵称",trigger:"blur"}]}}},methods:{getPersonInfo:function(e){var o=this;Object(l["h"])(e).then((function(e){200===e.status?(console.log(e),o.name=e.data.username,o.phone=e.data.mobile,""===e.data.email?o.email="未填写":o.email=e.data.email,o.password=e.data.password,o.ID=e.data.id,o.head=e.data.head):o.$message({message:"获取信息失败"+e.message,type:"error"})})).catch((function(e){console.log(e.response)}))},changeName:function(){var e=this;this.$refs.nameForm.validate((function(o){if(o){var t=n["a"];t.put("http://127.0.0.1:8000/users/"+localStorage.userId+"/",{username:e.nameForm.newName}).then((function(o){200===o.status?(console.log(o),e.name=e.nameForm.newName,e.$message({message:"修改昵称成功",type:"success"})):e.$message({message:"修改昵称失败",type:"error"})})).catch((function(e){console.log(e.response)}))}}))},changePhone:function(){var e=this;this.$refs.phoneForm.validate((function(o){if(o){var t=n["a"];t.put("http://127.0.0.1:8000/users/"+localStorage.userId+"/",{mobile:e.phoneForm.newPhone}).then((function(o){200===o.status?(console.log(o),e.phone=e.phoneForm.newPhone,e.$message({message:"修改昵称成功",type:"success"})):e.$message({message:"修改昵称失败",type:"error"})})).catch((function(e){console.log(e.response)}))}}))},changeEmail:function(){var e=this;this.$refs.emailForm.validate((function(o){if(o){var t=n["a"];t.put("http://127.0.0.1:8000/users/"+localStorage.userId+"/",{email:e.emailForm.newEmail}).then((function(o){200===o.status?(console.log(o),e.email=e.emailForm.newEmail,e.$message({message:"修改昵称成功",type:"success"})):e.$message({message:"修改昵称失败",type:"error"})})).catch((function(e){console.log(e.response)}))}}))}},mounted:function(){this.getPersonInfo(localStorage.userId)}},i=r,m=(t("4494"),t("2877")),c=Object(m["a"])(i,a,s,!1,null,null,null);o["default"]=c.exports},4494:function(e,o,t){"use strict";var a=t("ee28"),s=t.n(a);s.a},ee28:function(e,o,t){}}]);
//# sourceMappingURL=chunk-77b14560.7642dd1c.js.map