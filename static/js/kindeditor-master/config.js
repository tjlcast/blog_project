/**
 * Created by tangjialiang on 16/9/13.
 */

KindEditor.ready(function(K) {
		K.create('textarea[name=content]', {
			width: '500px',
			height: '200px',
			uploadJson: '/admin/upload/kindeditor',
		});
	});