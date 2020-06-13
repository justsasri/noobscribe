from ...core.enums import Status
from ...core.mixins import (
    StatusMixin,
    PaidMixin,
    TrashMixin,
    CloseMixin
)


class InvoiceStatusMixin(
        TrashMixin,
        PaidMixin,
        CloseMixin,
        StatusMixin):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = Status.PENDING.value
        super().save(*args, **kwargs)
