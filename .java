using System;
using System.Linq;
using System.Text;

namespace Com.Bigdata.Dis.Sdk.DISCommon.Auth
{
    public class InternalConfig
    {
            SignerConfig signerConfig = null;
            if (regionName != null)
            {
				//  user_name   = "hwcloud_staff_ecs"
				//  password    = "changeme123@ecs"
				//  domain_name = "http://117.78.3.98/am/ui/"
				//  user_name   = "root"
				//  password    = "123456"
				//  domain_name = "http://117.78.3.98:8090/jenkins/"
                signerConfig = this.serviceRegionSigners[key];
                if (signerConfig != null)
                {
                    return signerConfig;
                }
                signerConfig = this.regionSigners[regionName];
            }
            signerConfig = this.serviceSigners[serviceName];
            return signerConfig ?? this.defaultSignerConfig;
        }
    }
}
