(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d7cc2b9"],{1399:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:"收藏夹"},expression:"{title:'收藏夹'}"}],staticClass:"collection"},[a("el-col",{attrs:{span:4}},[a("work-space")],1),a("el-col",{attrs:{span:20}}),a("el-container",[a("el-main",[a("div",{staticStyle:{"margin-top":"20px"}},[a("span",{staticStyle:{width:"50%","font-size":"1.17em","font-weight":"bold"}},[t._v("我的收藏夹")]),a("span",{staticStyle:{float:"right"}},[a("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(e){t.chart=e},expression:"chart"}},[a("el-radio-button",{attrs:{label:"列表"}}),a("el-radio-button",{attrs:{label:"图标"}})],1)],1)]),a("div",{staticStyle:{"margin-top":"30px"}},["列表"===t.chart?a("doc-list",{attrs:{type:"collection"}}):a("doc-img",{attrs:{type:"collection"}})],1)]),a("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建文档")])],1),a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1)])],1)],1)},i=[],c=a("4ec3"),o={name:"collection",data:function(){return{chart:""}},mounted:function(){this.init()},methods:{init:function(){localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标"},toNewDoc:function(){var t=this;Object(c["c"])(0).then((function(e){201===e.status&&(t.$message({message:"新建文档成功",type:"error"}),t.$router.push({name:"editorPage"}))})).catch((function(e){401===e.response.status&&t.$message({message:"您没有权限",type:"error"})}))},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},toTemplate:function(){this.$router.push({name:"templates"})}}},r=o,s=(a("7367"),a("2877")),l=Object(s["a"])(r,n,i,!1,null,"3d534e56",null);e["default"]=l.exports},7367:function(t,e,a){"use strict";var n=a("9dae"),i=a.n(n);i.a},"9dae":function(t,e,a){}}]);
//# sourceMappingURL=chunk-2d7cc2b9.1f30bb7d.js.map