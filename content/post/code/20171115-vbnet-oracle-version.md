---
title: "[.NET] Sài nhiều phiên bản Oracle khi thực thi"
slug: vbnet-oracle-version
date: 2017-11-15T10:24:34+09:00
categories:
- Lập Trình
- .NET
tags:
- .NET
- OracleDB
keywords:
- VB.NET binding redirect
- Oracle VB.NET
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/vb.net.jpg
metaAlignment: center
---
Thông thường khi ta build ứng dụng thì phiên bản Oracle DB ở môi trường phát triển và môi trường thực thi là giống nhau nên không xảy ra vấn đề gì cả. Nhưng nếu ở môi trường phát triển và thực thi khác nhau thì sao?
<!--more-->

Khi đó khi chạy ứng dụng nó sẽ không khởi động được vì không tìm thấy phiên bản Oracle khi build ứng dụng đã sử dụng. Vậy ta phải làm thế nào?

Lúc ấy, ta cần làm 2 việc:

* 1. Không copy DLL của Oralce khi build mà sử dụng DLL của Oracle Client được cài đặt ở môi trường đích.
* 2. Thêm cấu hình `runtime` vào `App.config` của ứng dụng.

Việc thêm cấu hình `runtime` để giúp ứng dụng có thể linh động sử dụng các phiên bản DLL khác nhau. Trong trường hợp này là các phiên bản DLL của Oracle khác nhau như bên dưới đây.

```
<runtime>
	<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
		<dependentAssembly>
			<assemblyIdentity name="Oracle.DataAccess" publicKeyToken="89b483f429c47342" culture="neutral" />
			<publisherPolicy apply="no" />
			<bindingRedirect oldVersion="2.112.1.2" newVersion="4.112.4.0" />
		</dependentAssembly>
	</assemblyBinding>
</runtime>
```

Ở đoạn mã trên, ta cần chỉ định chính xác `name` và `publicKeyToken` của Oralce nếu không ứng dụng sẽ không thể tìm thấy được DLL tương ứng.

Điểm mấu chốt ở đây là cần thiết lập giá trị cho tag `bindingRedirect` cho chuẩn xác với:

* `oldVersion`: Phiên bản Oralce được sử dụng khi build ứng dụng
* `newVersion`: Phiên bản Oracle ở môi trường thực thi

Lưu ý là nếu môi trường thực thi có cùng phiên bản với môi trường phát triển thì ta vẫn cần chỉ rõ `newVersion` ở trên. Khi ấy, `newVersion` chính xác sẽ bằng với `oldVersion`.

Các giá trị này có thể lấy được bằng cách xem thông tin của DLL tương ứng trong mục `assembly` như hình mô tả dưới đây:

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vb.net-oracle-ver.png" title="Oracle Version Check">}}

Từ hình mô tả này ta có thể lấy được 3 thông tin về Oracle DLL như sau:

* `name`: *Oracle.DataAccess*
* `publicKeyToken`: *89b483f429c47342*
* `version`: *2.112.1.2*

Thực ra ngoài cách này ra, ta còn có thể viết code để thực hiện việc tham chiếu tới phiên bản Oracle mới, nhưng cách đó không linh động và đơn giản bằng cách trên nên tôi không đề cập ở đây.