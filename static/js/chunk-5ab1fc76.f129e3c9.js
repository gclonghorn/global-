(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5ab1fc76"],{"72a7":function(t,e,a){"use strict";var i=a("c2e8"),n=a.n(i);n.a},c2e8:function(t,e,a){},efcf:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:t.webTitle},expression:"{title:webTitle}"}],staticClass:"oneTeam"},[a("el-col",{attrs:{span:4}},[a("work-space")],1),a("el-col",{attrs:{span:20}}),a("el-container",[a("el-main",[a("div",{staticStyle:{position:"relative"}},[a("el-page-header",{on:{back:t.goBack}},[a("span",{attrs:{slot:"content"},slot:"content"},[t._v(t._s(t.teamName))])]),a("span",{staticStyle:{position:"absolute",right:"0",top:"0"}},[a("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(e){t.chart=e},expression:"chart"}},[a("el-radio-button",{attrs:{label:"列表"}}),a("el-radio-button",{attrs:{label:"图标"}})],1)],1)],1),a("div",{staticStyle:{"margin-top":"40px"}},["列表"===t.chart?a("doc-list",{attrs:{type:"team",team:t.teamId}}):a("doc-img",{attrs:{type:"team",team:t.teamId}})],1)]),a("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建团队文档")])],1),a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1),t.isBuilder?a("div",[a("el-button",{attrs:{plain:"",type:"primary"}},[t._v("管理团队")])],1):t._e(),a("div",[t.isBuilder?a("el-button",{attrs:{plain:"",type:"danger"}},[t._v("解散团队")]):a("el-button",{attrs:{plain:"",type:"danger"}},[t._v("退出团队")])],1)])],1)],1)},n=[],s=(a("b0c0"),a("4ec3")),r={name:"oneTeam",data:function(){return{webTitle:"团队文档",teamName:"",chart:"",isBuilder:!1,teamId:""}},mounted:function(){this.init()},methods:{init:function(){var t=this;localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标",this.teamId=this.$route.params.teamId,Object(s["p"])(this.teamId).then((function(e){200===e.status&&(t.teamName=e.data.name,t.webTitle=t.teamName+"的文档")})).catch((function(e){return t.$message({message:e.response.data,type:"error"})}))},toNewDoc:function(){var t=this;Object(s["f"])(0,"未命名",this.teamId).then((function(e){201===e.status&&(t.$message({message:"新建文档成功",type:"info"}),t.$router.push({name:"editorPage",params:{docId:e.data.id}}))})).catch((function(e){401===e.response.status&&t.$message({message:"您没有权限",type:"error"})}))},goBack:function(){this.$router.push({name:"myTeam"})},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},toTemplate:function(){this.$router.push({name:"templates",params:{teamId:this.teamId}})}}},o=r,c=(a("72a7"),a("2877")),l=Object(c["a"])(o,i,n,!1,null,"3466711f",null);e["default"]=l.exports}}]);
//# sourceMappingURL=chunk-5ab1fc76.f129e3c9.js.map