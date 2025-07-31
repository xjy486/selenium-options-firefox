    # --- 核心运行参数 ---
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    # --- 关键：启用私密（无痕）浏览模式 ---
    # 这确保了不会保存历史记录、Cookie 或缓存到磁盘。
    options.add_argument('-private-window')

    # --- 关键：强制禁用所有形式的缓存 ---
    # 双重保险，确保资源总是从服务器重新加载。
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("browser.cache.offline.enable", False)
    options.set_preference("network.http.use-cache", False)

    # --- 浏览器启动与主页设置 ---
    options.set_preference("browser.startup.page", 1)
    options.set_preference("browser.startup.homepage", "about:blank")
    options.set_preference("startup.homepage_welcome_url", "about:blank")
    options.set_preference("startup.homepage_welcome_url.additional", "about:blank")

    # --- 禁用遥测、数据报告和崩溃报告 ---
    options.set_preference("toolkit.telemetry.enabled", False)
    options.set_preference("toolkit.telemetry.unified", False)
    options.set_preference("toolkit.telemetry.server", "data:application/json,{}")
    options.set_preference("datareporting.healthreport.uploadEnabled", False)
    options.set_preference("datareporting.policy.dataSubmissionEnabled", False)

    # --- 禁用浏览器更新、安全检查和远程设置 ---
    options.set_preference("app.update.auto", False)
    options.set_preference("app.update.enabled", False)
    options.set_preference("app.update.checkInstallTime", False)
    options.set_preference("app.update.service.enabled", False)
    options.set_preference("app.normandy.api_url", "")
    options.set_preference("browser.safebrowsing.enabled", False)
    options.set_preference("browser.safebrowsing.phishing.enabled", False)
    options.set_preference("browser.safebrowsing.malware.enabled", False)
    options.set_preference("browser.safebrowsing.downloads.enabled", False)
    options.set_preference("browser.safebrowsing.downloads.remote.enabled", False)
    options.set_preference("security.remote_settings.crlite_filters.enabled", False)
    options.set_preference("security.remote_settings.intermediates.enabled", False)
    options.set_preference("security.remote_settings.OneCRL.enabled", False)
    options.set_preference("security.remote_settings.addons.enabled", False)
    options.set_preference("security.remote_settings.pinning.enabled", False)
    options.set_preference("security.remote_settings.features.enabled", False)
    options.set_preference("services.settings.server", "")

    # --- 禁用网络连接相关的“智能”功能和预加载 ---
    options.set_preference("network.prefetch-next", False)
    options.set_preference("network.dns.disablePrefetch", True)
    options.set_preference("network.predictor.enabled", False)
    options.set_preference("network.http.speculative-parallel-limit", 0)
    options.set_preference("network.captive-portal-service.enabled", False)
    options.set_preference("network.connectivity-service.enabled", False)
    options.set_preference("browser.fixup.alternate.enabled", False) # 禁用自动修正 URL

    # --- 禁用 Firefox 集成服务 (Pocket, 新标签页推荐等) ---
    options.set_preference("extensions.pocket.enabled", False)
    options.set_preference("extensions.pocket.api", "")
    options.set_preference("browser.newtabpage.activity-stream.feeds.section.topstories", False)
    options.set_preference("browser.newtabpage.activity-stream.feeds.topsites", False)
    options.set_preference("browser.newtabpage.activity-stream.feeds.system.topsites", False)
    options.set_preference("browser.selfsupport.url", "")
    options.set_preference("browser.aboutHomeSnippets.updateUrl", "")

    # --- 禁用附加组件相关的更新和阻止列表 ---
    options.set_preference("extensions.update.enabled", False)
    options.set_preference("extensions.blocklist.enabled", False)

    # --- 禁用搜索建议 ---
    options.set_preference("browser.search.suggest.enabled", False)
    options.set_preference("keyword.enabled", False) # 禁用地址栏关键字搜索

    # --- 禁用证书验证相关的网络请求 (OCSP, CRL) ---
    # 这会减少启动和页面加载时的背景请求，但在某些情况下可能存在安全风险。
    options.set_preference("security.OCSP.enabled", 0)
    options.set_preference("security.OCSP.require", False)
    options.set_preference("security.cert_pinning.process_headers", False)
    options.set_preference("security.crlite_mode", 0)
    options.set_preference("security.ssl.enable_ocsp_stapling", False)
    options.set_preference("security.ssl.enable_ocsp_must_staple", False)
    options.set_preference("security.ssl.enable_post_handshake_auth", False)
    options.set_preference("security.content.signature.root_hash", "")

    # --- 可选：完全跳过证书错误（仅在受信任的测试环境中使用！）---
    options.set_preference("accept_insecure_certs", True)
