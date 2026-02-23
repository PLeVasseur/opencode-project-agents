# PR #77: Clarification on Subscriber UUri Resource ID in Test Data

## Question

In test fixtures such as:

```text
subscription("//authority-a/5BA1/1/8001", "//authority-b/5678/1/1234")
```

should the subscriber UUri use resource `0x0000` instead of `0x1234` for clarity?

## Short Answer

Yes, using subscriber resource `0x0000` is clearer and better aligned with uProtocol endpoint semantics.

However, the current uSubscription specification does **not** state an explicit MUST that `SubscriberInfo.uri.resource_id == 0`. It requires a valid non-wildcard subscriber URI.

## Spec Citations

1. **`SubscriberInfo` models the subscribing uEntity identity**
   - `SubscriberInfo` is described as subscriber identification info, i.e. URI of the uEntity subscribing.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/up-core-api/uprotocol/core/usubscription/v3/usubscription.proto#L120-L124

2. **Fetch by subscriber is subscriber -> topics**
   - `FetchSubscriptions(SubscriberInfo)` returns topics currently subscribed to by that subscriber.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/up-l3/usubscription/v3/README.adoc#L242-L245
     - Spec item: `req~usubscription-fetch-subscriptions-by-subscriber~1`

3. **Subscriber URI validity rule (no wildcards, including resource wildcard)**
   - Subscriber URI in `FetchSubscriptions` must be valid and must not contain wildcard authority/ue_id/resource.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/up-l3/usubscription/v3/README.adoc#L264-L273
     - Spec item: `dsn~usubscription-fetch-subscriptions-invalid-subscriber~1`

4. **`resource_id` means resource/method identifier**
   - A UUri `resource_id` identifies the resource or method being referred to.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/basics/uri.adoc#L114-L117
     - Spec item: `dsn~uri-resource-id~1`

5. **Endpoint-style receiver semantics consistently use resource `0`**
   - Notification sink resource MUST be `0`.
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/basics/uattributes.adoc#L263-L266
     - Spec item: `dsn~up-attributes-notification-sink~1`
   - RPC request source resource MUST be `0`.
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/basics/uattributes.adoc#L293-L296
     - Spec item: `dsn~up-attributes-request-source~1`
   - RPC response sink resource MUST be `0`.
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/basics/uattributes.adoc#L384-L387
     - Spec item: `dsn~up-attributes-response-sink~1`

6. **Publish topic resources are in event range, not endpoint 0**
   - Publish source resource MUST be in `[0x8000, 0xFFFE]`.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/basics/uattributes.adoc#L213-L216
     - Spec item: `dsn~up-attributes-publish-source~1`

7. **Remote subscription context emphasizes uEntity identity**
   - Remote subscriptions are performed between uSubscription services using their own uEntity identifiers.
   - Citation:
     - https://github.com/eclipse-uprotocol/up-spec/blob/main/up-l3/usubscription/v3/README.adoc#L569

## Conclusion for PR Comment

- The reviewer suggestion to use subscriber resource `0x0000` improves readability and better communicates "subscriber endpoint identity" semantics.
- This is a **clarity/convention** improvement rather than a strict conformance fix, because current usubscription text does not explicitly require subscriber resource `0`.
- If desired, we can also open an up-spec follow-up to make this explicit for `SubscriberInfo.uri`.

## Suggested Comment Text

> Good point. We checked `up-spec` and agree this is clearer with subscriber resource `0x0000`.
>
> `SubscriberInfo` is modeled as subscriber uEntity identity (`usubscription.proto`), and endpoint-style receiver addresses in uProtocol consistently use resource `0` (notification sink, request source, response sink in `basics/uattributes.adoc`).
>
> The current usubscription spec explicitly requires valid non-wildcard subscriber URIs, but does not yet add an explicit MUST that `SubscriberInfo.uri.resource_id == 0`.
>
> So we should treat this as a clarity/convention improvement in tests and consider an up-spec follow-up to codify it explicitly.
