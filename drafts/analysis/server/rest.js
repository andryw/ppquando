//Programacao = new Mongo.Collection("programacao");

//
//if (Meteor.isServer) {
//	console.log('abc');
//  Restivus.addCollection(Programacao);
//
//  // Maps to: /api/posts/:id
//  Restivus.addRoute('api/raiox/:data', {
//    get: function () {
//	console.log('oi');
//      var post = Programacao.findOne(this.urlParams.data);
//      if (post) {
//	console.log(post);
//        return {status: 'success', data: post};
//      }
//      return {
//        statusCode: 404,
//        body: {status: 'fail', message: 'Post not found'}
//      };
//    }
//  });
//
//}
