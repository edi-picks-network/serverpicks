import { useEffect } from 'react';
import { organizationSchema } from '@/lib/schema';

interface JsonLdProps {
  siteName?: string;
  siteUrl?: string;
  description?: string;
}

export default function JsonLd({
  siteName = 'ServerPicks',
  siteUrl = 'https://serverpicks.net',
  description = 'Cloud infrastructure benchmarking and hosting comparison guides from Boston, MA.',
}: JsonLdProps) {
  useEffect(() => {
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.text = JSON.stringify(
      organizationSchema(siteName, siteUrl, description)
    );
    document.head.appendChild(script);
    return () => {
      document.head.removeChild(script);
    };
  }, [siteName, siteUrl, description]);

  return null;
}
