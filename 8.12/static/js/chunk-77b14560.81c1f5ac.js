(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-77b14560"],{"1bf9":function(e,o,t){"use strict";t.r(o);var a=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",{staticClass:"basic"},[t("el-col",{attrs:{span:4}},[t("work-space")],1),t("el-col",{attrs:{span:20}}),t("div",{staticClass:"box"},[t("el-card",{staticStyle:{"background-color":"whitesmoke",border:"0px"},attrs:{shadow:"never"}},[t("br"),t("el-row",[t("el-col",{attrs:{span:8}},[t("el-row",[t("el-avatar",{attrs:{size:80,src:e.circleUrl}})],1),t("br"),t("el-row",[t("el-button",{attrs:{type:"text",icon:"el-icon-edit"}},[e._v("修改头像")])],1)],1),t("el-col",{attrs:{span:4}},[t("el-form",[t("el-form-item",[t("i",{staticClass:"el-icon-user-solid"},[e._v(" 昵称")])]),t("el-form-item",[t("i",{staticClass:"el-icon-paperclip"},[e._v(" 密码")])]),t("el-form-item",[t("i",{staticClass:"el-icon-phone"},[e._v(" 手机")])]),t("el-form-item",[t("i",{staticClass:"el-icon-message"},[e._v(" 邮箱")])]),t("el-form-item",[t("i",{staticClass:"el-icon-s-flag"},[e._v(" 账号ID")])])],1)],1),t("el-col",{attrs:{span:8}},[t("el-form",[t("el-form-item",[e._v(e._s(e.name))]),t("el-form-item",[e._v("********")]),t("el-form-item",[e._v(e._s(e.phone))]),t("el-form-item",[e._v(e._s(e.email)+" ")]),t("el-form-item",[e._v(e._s(e.ID))])],1)],1),t("el-col",{attrs:{span:2}},[t("el-form",[t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changeNameVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改昵称",visible:e.changeNameVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changeNameVisible=o}}},[t("el-form",{attrs:{model:e.nameForm}},[t("el-form-item",[t("el-input",{attrs:{autocomplete:"off",placeholder:"新昵称"},model:{value:e.nameForm.newName,callback:function(o){e.$set(e.nameForm,"newName",o)},expression:"nameForm.newName"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changeNameVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:function(o){e.changeNameVisible=!1}}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changePasswordVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改密码",visible:e.changePasswordVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changePasswordVisible=o}}},[t("el-form",{attrs:{model:e.passwordForm}},[t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"当前密码"},model:{value:e.passwordForm.currentPassword,callback:function(o){e.$set(e.passwordForm,"currentPassword",o)},expression:"passwordForm.currentPassword"}})],1),t("br"),t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"新密码"},model:{value:e.passwordForm.newPassword,callback:function(o){e.$set(e.passwordForm,"newPassword",o)},expression:"passwordForm.newPassword"}})],1),t("br"),t("el-form-item",[t("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"确认新密码"},model:{value:e.passwordForm.newPasswordAgain,callback:function(o){e.$set(e.passwordForm,"newPasswordAgain",o)},expression:"passwordForm.newPasswordAgain"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changePasswordVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:function(o){e.changePasswordVisible=!1}}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changePhoneVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改手机号",visible:e.changePhoneVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changePhoneVisible=o}}},[t("el-form",{attrs:{model:e.phoneForm}},[t("el-form-item",[t("el-input",{attrs:{type:"tel",autocomplete:"off",placeholder:"新手机号"},model:{value:e.phoneForm.newPhone,callback:function(o){e.$set(e.phoneForm,"newPhone",o)},expression:"phoneForm.newPhone"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changePhoneVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:function(o){e.changePhoneVisible=!1}}},[e._v("确 定")])],1)],1)],1),t("el-form-item",[t("el-button",{attrs:{type:"text"},on:{click:function(o){e.changeEmailVisible=!0}}},[e._v("修改")]),t("el-dialog",{attrs:{title:"修改邮箱",visible:e.changeEmailVisible,"modal-append-to-body":!1,width:"300px"},on:{"update:visible":function(o){e.changeEmailVisible=o}}},[t("el-form",{attrs:{model:e.emailForm}},[t("el-form-item",[t("el-input",{attrs:{type:"tel",autocomplete:"off",placeholder:"新邮箱"},model:{value:e.emailForm.newEmail,callback:function(o){e.$set(e.emailForm,"newEmail",o)},expression:"emailForm.newEmail"}})],1)],1),t("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-button",{on:{click:function(o){e.changeEmailVisible=!1}}},[e._v("取 消")]),t("el-button",{attrs:{type:"primary"},on:{click:function(o){e.changeEmailVisible=!1}}},[e._v("确 定")])],1)],1)],1)],1)],1)],1)],1)],1)],1)},l=[],s={data:function(){return{name:"whisper",password:"123123",phone:"18538947201",email:"1214960505@qq.com",ID:"18373154",circleUrl:"https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",changePasswordVisible:!1,changePhoneVisible:!1,changeEmailVisible:!1,changeNameVisible:!1,passwordForm:{currentPassword:"",newPassword:"",newPasswordAgain:""},phoneForm:{newPhone:""},emailForm:{newEmail:""},nameForm:{newName:""}}},methods:{toChangeInfo:function(){this.$router.push({path:"/ChangeInfo"})}}},i=s,n=(t("4494"),t("2877")),r=Object(n["a"])(i,a,l,!1,null,null,null);o["default"]=r.exports},4494:function(e,o,t){"use strict";var a=t("ee28"),l=t.n(a);l.a},ee28:function(e,o,t){}}]);
//# sourceMappingURL=chunk-77b14560.81c1f5ac.js.map