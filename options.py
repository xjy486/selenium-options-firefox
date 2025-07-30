				options.set_preference("services.settings.server", "")
        options.set_preference("services.settings.default_bucket", "")
        options.set_preference("services.settings.default_signer", "")
        options.set_preference("services.settings.load_from_file", True)  # 强制从本地加载
        options.set_preference("services.settings.remote_settings.enabled", False)
        # 1. 禁用遥测和数据报告
        options.set_preference("toolkit.telemetry.enabled", False)
        options.set_preference("toolkit.telemetry.unified", False)
        options.set_preference("toolkit.telemetry.server", "data:application/json,{}")
        options.set_preference("datareporting.healthreport.uploadEnabled", False)
        options.set_preference("datareporting.policy.dataSubmissionEnabled", False)

        # 2. 禁用浏览器更新和安全检查
        options.set_preference("app.update.auto", False)
        options.set_preference("app.update.enabled", False)
        options.set_preference("app.update.checkInstallTime", False)
        options.set_preference("app.update.service.enabled", False)
        options.set_preference("app.normandy.api_url","")
        options.set_preference("browser.safebrowsing.enabled", False)
        options.set_preference("browser.safebrowsing.phishing.enabled", False)
        options.set_preference("browser.safebrowsing.malware.enabled", False)
        options.set_preference("browser.safebrowsing.downloads.enabled", False)
        options.set_preference("browser.safebrowsing.downloads.remote.enabled", False)
        options.set_preference("browser.selfsupport.url", "")
        options.set_preference("browser.aboutHomeSnippets.updateUrl", "")
        # 📦 禁用附加组件相关的远程设置
        options.set_preference("browser.newtabpage.activity-stream.feeds.section.topstories", False)
        options.set_preference("browser.newtabpage.activity-stream.feeds.topsites", False)
        options.set_preference("browser.newtabpage.activity-stream.feeds.system.topsites", False)
        # 3. 禁用网络连接相关的“智能”功能
        options.set_preference("network.prefetch-next", False)
        options.set_preference("network.dns.disablePrefetch", True)
        options.set_preference("network.predictor.enabled", False)
        options.set_preference("network.captive-portal-service.enabled", False)  # 禁用网络连接探测
        options.set_preference("network.connectivity-service.enabled", False)
        options.set_preference("network.http.speculative-parallel-limit", 0)
        # 4. 禁用 Firefox "Pocket" 和其他集成服务
        options.set_preference("extensions.pocket.enabled", False)
        options.set_preference("extensions.pocket.api", "")
        options.set_preference("extensions.update.enabled", False)
        options.set_preference("extensions.blocklist.enabled", False)
        # 5. 禁用搜索建议
        options.set_preference("browser.search.suggest.enabled", False)
        # 禁用内容签名
        options.set_preference("security.content.signature.root_hash", "")

        # 禁用健康报告
        options.set_preference("datareporting.healthreport.uploadEnabled", False)
        options.set_preference("datareporting.policy.dataSubmissionEnabled", False)
        #
        options.set_preference("browser.startup.page", 1)
        options.set_preference("browser.startup.homepage", "about:blank")
        options.set_preference("startup.homepage_welcome_url", "about:blank")
        options.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        # 🔐 禁用 OCSP 查询（最关键的一步）
        options.set_preference("security.OCSP.enabled", 0)  # 0 = 完全禁用
        options.set_preference("security.OCSP.require", False)  # 不强制要求 OCSP

        # 📦 禁用 CRL（证书吊销列表）下载
        options.set_preference("security.cert_pinning.process_headers", False)
        options.set_preference("security.crlite_mode", 0)  # 禁用 CRLite（Firefox 89+ 的新机制）

        # 🌐 禁用安全功能（可选，进一步减少背景请求）
        options.set_preference("security.ssl.enable_ocsp_stapling", False)  # 禁用 OCSP Stapling
        options.set_preference("security.ssl.enable_ocsp_must_staple", False)
        options.set_preference("security.ssl.enable_post_handshake_auth", False)

        # 🕵️ 隐私相关（减少跟踪和预加载）
        options.set_preference("network.http.speculative-parallel-limit", 0)  # 禁用预连接
        options.set_preference("browser.fixup.alternate.enabled", False)  # 禁用自动修正 URL
        options.set_preference("keyword.enabled", False)  # 禁用关键字搜索

        # 🚫 可选：完全跳过证书错误（仅用于测试环境！）
        options.set_preference("webdriver_accept_untrusted_certs", True)
        options.set_preference("webdriver_assume_untrusted_issuer", True)
        options.set_preference("accept_insecure_certs", True)
        # 禁用安全列表远程更新
        options.set_preference("security.remote_settings.crlite_filters.enabled", False)
        options.set_preference("security.remote_settings.intermediates.enabled", False)
        options.set_preference("security.remote_settings.OneCRL.enabled", False)
        options.set_preference("security.remote_settings.addons.enabled", False)
        options.set_preference("security.remote_settings.pinning.enabled", False)
        options.set_preference("security.remote_settings.features.enabled", False)
