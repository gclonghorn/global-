(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a59b9bd8"],{"43c4":function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"history"},[a("el-col",{attrs:{span:4}},[a("work-space")],1),a("el-col",{attrs:{span:20}}),a("el-container",[a("el-main",[a("div",{staticStyle:{"margin-top":"20px"}},[a("span",{staticStyle:{width:"50%","font-size":"1.17em","font-weight":"bold"}},[t._v("最近浏览")]),a("span",{staticStyle:{float:"right"}},[a("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(e){t.chart=e},expression:"chart"}},[a("el-radio-button",{attrs:{label:"列表"}}),a("el-radio-button",{attrs:{label:"图标"}})],1)],1)]),a("div",{staticStyle:{"margin-top":"30px"}},["列表"===t.chart?a("doc-list",{attrs:{type:"history"}}):a("doc-img",{attrs:{type:"history"}})],1)]),a("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建文档")])],1),a("folder-dialog",{attrs:{"dialog-form-visible":t.folderDialog},on:{changeVisible:t.changeVisible}}),a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1)],1)],1)],1)},o=[],n=(a("4160"),a("b0c0"),a("159b"),a("4ec3")),c={name:"history",data:function(){return{chart:"",folderDialog:!1,docList:[]}},mounted:function(){this.init()},methods:{init:function(){var t=this;Object(n["d"])(1).then((function(e){200===e.status&&(0===e.data.length?t.docList=[]:e.data.forEach((function(e){t.docList=[],t.docList.push({docId:e.document.id,docName:e.document.name,readTime:e.read_time})})))})).catch((function(e){t.$message({message:e,type:"error"})})),localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标"},toNewDoc:function(){this.$router.push({name:"editorPage"})},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},changeVisible:function(t){this.folderDialog=t},toTemplate:function(){this.$router.push({name:"templates"})}}},r=c,s=(a("adee"),a("2877")),l=Object(s["a"])(r,i,o,!1,null,"3605ee85",null);e["default"]=l.exports},ab85:function(t,e,a){},adee:function(t,e,a){"use strict";var i=a("ab85"),o=a.n(i);o.a}}]);
//# sourceMappingURL=chunk-a59b9bd8.9513e1ee.js.map