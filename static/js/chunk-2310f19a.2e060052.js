(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2310f19a"],{"915b":function(t,a,e){"use strict";var n=e("c864"),i=e.n(n);i.a},c864:function(t,a,e){},efcf:function(t,a,e){"use strict";e.r(a);var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"oneTeam"},[e("el-col",{attrs:{span:4}},[e("work-space")],1),e("el-col",{attrs:{span:20}}),e("el-container",[e("el-main",[e("div",{staticStyle:{position:"relative"}},[e("el-page-header",{on:{back:t.goBack}},[e("span",{attrs:{slot:"content"},slot:"content"},[t._v(t._s(t.teamName))])]),e("span",{staticStyle:{position:"absolute",right:"0",top:"0"}},[e("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(a){t.chart=a},expression:"chart"}},[e("el-radio-button",{attrs:{label:"列表"}}),e("el-radio-button",{attrs:{label:"图标"}})],1)],1)],1),e("div",{staticStyle:{"margin-top":"40px"}},["列表"===t.chart?e("doc-list",{attrs:{type:"team",team:t.teamId}}):e("doc-img",{attrs:{type:"team",team:t.teamId}})],1)]),e("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[e("div",[e("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建文档")])],1),e("div",[e("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1),t.isBuilder?e("div",[e("el-button",{attrs:{plain:"",type:"primary"}},[t._v("管理团队")])],1):t._e(),e("div",[t.isBuilder?e("el-button",{attrs:{plain:"",type:"danger"}},[t._v("解散团队")]):e("el-button",{attrs:{plain:"",type:"danger"}},[t._v("退出团队")])],1)])],1)],1)},i=[],o={name:"oneTeam",data:function(){return{teamName:"团队1",chart:"",isBuilder:!1,teamId:""}},mounted:function(){this.init()},methods:{init:function(){localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标",this.teamId=this.$route.params.teamId},toNewDoc:function(){this.$router.push({name:"editorPage"})},goBack:function(){this.$router.push({name:"myTeam"})},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},toTemplate:function(){this.$router.push({name:"templates"})}}},r=o,s=(e("915b"),e("2877")),c=Object(s["a"])(r,n,i,!1,null,"77badaa5",null);a["default"]=c.exports}}]);
//# sourceMappingURL=chunk-2310f19a.2e060052.js.map